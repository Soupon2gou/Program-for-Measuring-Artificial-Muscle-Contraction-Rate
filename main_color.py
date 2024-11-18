import cv2
import numpy as np
import sys
# 画像読み込み
image_path = ".\\resources\\hi_kukkyoku_color.jpg"  # 画像のパス
# image_path = "black.png"  # 画像のパス
image = cv2.imread(image_path)  # 画像の読み込み
if image is None:
    raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
# 元画像をコピーしておく
image_copy = image.copy()
# RGBからHSVに変換
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

########################################################################
# imageにおいて赤色を全探索して、その座標を取得する
# 赤色の閾値を設定
lower_red1 = np.array([0, 100, 100])   # 下限 (色相, 彩度, 明度)
upper_red1 = np.array([10, 255, 255]) # 上限

# 赤色の部分をimageから取得
mask = cv2.inRange(image, lower_red1, upper_red1)

# 赤色の部分をimageから取得
red = cv2.bitwise_and(image, image, mask=mask) #bitwise_and(元画像, 元画像, マスク画像)

# 赤色の部分の位置を取得
red_pos = np.where(mask == 255)

# 赤色の部分の位置をcopy_imageに描画
image_copy[red_pos[0], red_pos[1]] = [0, 0, 255]

########################################################################
# 青色の部分を全探索して、その座標を取得する
# 青色の閾値を設定
lower_blue1 = np.array([100, 80, 40])   # 下限 (色相, 彩度, 明度)
upper_blue1 = np.array([130, 255, 255]) # 上限


# 青色の部分をimageから取得
mask = cv2.inRange(image, lower_blue1, upper_blue1)

# 青色の部分をimageから取得
blue = cv2.bitwise_and(image, image, mask=mask)

# 青色の部分の位置を取得
blue_pos = np.where(mask == 255)

# 青色の部分の位置をimage_copyに描画
image_copy[blue_pos[0], blue_pos[1]] = [255, 0, 0]

########################################################################
# 赤色の中心座標を取得
red_pos = np.array([int(red_pos[0].mean()), int(red_pos[1].mean())])

# 青色の座標を取得
blue_pos = np.array([int(blue_pos[0][0].mean()), int(blue_pos[1][0].mean())])

print(f"赤色の座標: {red_pos}")
print(f"青色の座標: {blue_pos}")
########################################################################

#赤色の座標に〇を描画 red_posは(y,x)の順番なので、(x,y)に変換
cv2.circle(image_copy, tuple(red_pos[::-1]), 1, (0, 0, 255), 5) # (画像, 中心座標(y,x), 半径, 色(B,G,R), 線の太さ)

#青色の座標に〇を描画 blue_posは(y,x)の順番なので、(x,y)に変換
cv2.circle(image_copy, tuple(blue_pos[::-1]), 1, (255, 0, 0), 5) # (画像, 中心座標(y,x), 半径, 色(B,G,R), ��の太さ)

################################################################
# 画像を保存
cv2.imwrite("output.jpg", image_copy)
# 画像を表示
cv2.imshow("image", image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()