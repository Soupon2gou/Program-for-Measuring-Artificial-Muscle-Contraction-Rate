import cv2
import numpy as np
import sys
# 画像読み込み
image_path = ".\\resources\\hi_kukkyoku.jpg"  # 画像のパス
# image_path = "black.png"  # 画像のパス
image = cv2.imread(image_path)  # 画像の読み込み
if image is None:
    raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
#画像のリサイズHD画質に変換
image = cv2.resize(image, dsize=(1280,720))
# 元画像をコピーしておく
image_copy = image.copy()
# RGBからHSVに変換
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 画像を表示
cv2.imshow("image", image)
cv2.waitKey(0)
########################################################################
# imageにおいて赤色を全探索して、その座標を取得する
# 赤色の閾値を設定
lower_red1 = np.array([0, 120, 70])   # 下限 (色相, 彩度, 明度)
upper_red1 = np.array([10, 255, 255]) # 上限

# 赤色の部分をimageから取得
mask = cv2.inRange(image, lower_red1, upper_red1)

#　bitwise_andを使うには2つの画像サイズ + タイプが同じである必要がある。
# print(img1.shape, img2.shape), print(type(img1), type(img2))して、値が等しいことを確認
# 画像のサイズを確認
print(image.shape, mask.shape)

# 赤色の部分をimageから取得
red = cv2.bitwise_and(image, image, mask=mask) #bitwise_and(元画像, 元画像, マスク画像)

# 赤色の部分の位置を取得
red_pos = np.where(mask == 255)

# 赤色の部分の位置をcopy_imageに描画
image_copy[red_pos[0], red_pos[1]] = [0, 0, 255]
print(red_pos)

########################################################################
# 青色の部分を全探索して、その座標を取得する
# 青色の閾値を設定
lower_blue1 = np.array([100, 50, 50])   # 下限 (色相, 彩度, 明度)
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
#前提として赤色の座標はただ一つと仮定
#赤色の座標を取得
red_pos = np.array([red_pos[0][0], red_pos[1][0]])
# red_posが画像の範囲外の場合
if red_pos[0] >= image_copy.shape[0] or red_pos[1] >= image_copy.shape[1]:
    raise ValueError("赤色の座標が画像の範囲外です")

#青色の座標を取得
blue_pos = np.array([blue_pos[0][0], blue_pos[1][0]])

print(f"赤色の座標: {red_pos}")
print(f"青色の座標: {blue_pos}")

#赤色の座標に〇を描画
cv2.circle(image_copy, tuple(red_pos), 100, (0, 0, 255), 100) # (画像, 中心座標, 半径, 色, 線の太さ)

#青色の座標に〇を描画
cv2.circle(image_copy, tuple(blue_pos), 10, (255, 0, 0), 100) # (画像, 中心座標, 半径, 色, 線の太さ)

#赤色と青色の座標を結ぶ直線を引く
# cv2.line(image, tuple(red_pos), tuple(blue_pos), (0, 255, 0), 1000) # 直線を引く (画像, 始点, 終点, 色, 太さ)

################################################################
# 画像を保存
cv2.imwrite("output.jpg", image_copy)
# 画像を表示
cv2.imshow("image", image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()