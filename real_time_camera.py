import cv2
# print(cv2)

#cameraでリアルタイムに画像を取得する場合は、以下のコードを使う
cap = cv2.VideoCapture(0)

image = cv2.resize(cap, dsize=(1920, 1080))

#　グレースケール変換
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 表示
# cv2.imshow("gray_image", gray_image)

# 画像のトリミング
trimmed_image = gray_image[380:460, 450:1350]

trimmed_image_width = trimmed_image.shape[1]

#画像をある閾値で白と黒に分ける

_, trimmed_image = cv2.threshold(trimmed_image, 50, 255, cv2.THRESH_BINARY)  # ��値127で白と��に分ける

# 画像を表示
cv2.imshow("trimmed_image", trimmed_image)


#findstartpointという関数を作成
def findstartpoint(trimmed_image):
    trimmed_image_width = trimmed_image.shape[1]
    for b in range(0, 256):  # 0から255までの値で探索       
        for x in range(5,trimmed_image_width,1):
            for y in range(trimmed_image.shape[0]):
                if trimmed_image[y, x] == b:  # 黒めのピクセルを見つけたら
                    start_point = (x, y)
                    print("color_number: ", b)
                    return start_point

#左端から上下にピクセルを全探索して黒だったらそこを始点とする
start_point = findstartpoint(trimmed_image)
                

#findendpointという関数を作成

def findendpoint(trimmed_image):
    trimmed_image_width = trimmed_image.shape[1]
    for b in range(0, 256):  # 0から255までの値で探索
        for x in range(trimmed_image_width - 6, -1, -1): #rangeの因数の意味は、(開始位置, 終了位置, ステップ)で、-1は��順を意味する
            for y in range(trimmed_image.shape[0]):
                if trimmed_image[y, x] == b:  # ��いピクセルを見つけたら
                    end_point = (x, y)
                    print("color_number: ", b)
                    return end_point
                
#右端から上下にピクセルを全探索して黒だったらそこを終点とする
end_point = findendpoint(trimmed_image)

    # 結果を表示
if start_point and end_point:
    print(f"始点: {start_point}, 終点: {end_point}")
else:
    print("黒いピクセルが見つかりませんでした")

# 始点と終点の色を変えてtrimmed_imageを表示
if start_point:
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            y = start_point[1] + dy
            x = start_point[0] + dx
            if 0 <= y < trimmed_image.shape[0] and 0 <= x < trimmed_image.shape[1]:
                # 始点の周り9ピクセルを赤にする
                trimmed_image[y, x] = 127

if end_point:
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            y = end_point[1] + dy
            x = end_point[0] + dx
            if 0 <= y < trimmed_image.shape[0] and 0 <= x < trimmed_image.shape[1]:
                trimmed_image[y, x] = 127  # 終点の周り9ピクセルを

# トリミングした画像を表示

cv2.imshow("trimmed_image", trimmed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()