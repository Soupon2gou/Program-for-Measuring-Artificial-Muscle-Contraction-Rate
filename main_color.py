import cv2
import numpy as np
import threepoint_all_position as thpy
# print(cv2)

# 画像読み込み
image_path = ".\\resources\\hi_kukkyoku.jpg"  # 画像のパス
# image_path = "black.png"  # 画像のパス
image = cv2.imread(image_path)  # 画像の読み込み
#画像の解像度をHHDに変更
image = cv2.resize(image, dsize=(1920, 1080))
if image is None:
    raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
# 画像のトリミング
trimmed_image = image[400:460, 490:1400]
trimmed_image_width = trimmed_image.shape[1]

########################################################################
# 画像の初期処理
th =70
# グレースケール変換
trimmed_image = cv2.cvtColor(trimmed_image, cv2.COLOR_BGR2GRAY)

#threepoint_all_position.pyのリストを取得して不要な範囲を白にする
#ファイルの読み込み
# white_list= thpy.pixels
# for pixel in white_list:
#     trimmed_image[pixel[1], pixel[0]] = 255

#ガウシアンフィルタをかける
trimmed_image = cv2.GaussianBlur(trimmed_image, (5, 5), 0)

# 二値化
_, trimmed_image = cv2.threshold(trimmed_image, th, 255, cv2.THRESH_BINARY)
# cv2.imshow("binary", trimmed_image)

#edge detection

# edges = cv2.Canny(trimmed_image, 100, 200)

# show edge detection

# cv2.imshow("edges", edges)

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