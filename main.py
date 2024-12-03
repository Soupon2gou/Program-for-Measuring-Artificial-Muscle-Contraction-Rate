import cv2
import numpy as np
import sys
from find_point import find_point
from calculate_length import calculate_length

# 画像読み込み
image_path = ".\\resources\\hi_kukkyoku_color2.jpg"  # 画像のパス
# image_path = "black.png"  # 画像のパス
image = cv2.imread(image_path)  # 画像の読み込み
if image is None:
    raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
# 画像のコピー
image_copy = image.copy()
################################################################
# メイン処理
# find_point.pyよりred_posとblue_posを取得
red_center_pos, green_center_pos, blue_center_pos = find_point(image)
print(f"red_center_pos: {red_center_pos}")
print(f"blue_center_pos: {blue_center_pos}")
print(f"green_center_pos: {green_center_pos}")

# 長さを計算
hik_length, k_length = calculate_length(
    red_center_pos, green_center_pos, blue_center_pos, image
)
# k_length = 800.0
print(f"hi_kukkyoku_length: {hik_length}")
print(f"k_length: {k_length}")
################################################################
# 収縮率計算
# 収縮率 = (hi_kukkyoku_length / k_length) * 100

shrink_rate = 1.0 - (k_length / hik_length)
# 百分率に変換
shrink_rate *= 100
print(f"収縮率: {shrink_rate:.2f}%")

################################################################
# image_copyに描画と表示
# 座標を整数に変換
red_center_pos = tuple(map(int, red_center_pos))
green_center_pos = tuple(map(int, green_center_pos))
blue_center_pos = tuple(map(int, blue_center_pos))
# 赤色の座標に〇を描画 red_posは(y,x)の順番なので、(x,y)に変換
cv2.circle(
    image_copy, tuple(red_center_pos[::-1]), 1, (0, 0, 255), 5
)  # (画像, 中心座標(y,x), 半径, 色(B,G,R), 線の太さ)

# 緑色の座標に〇を描画 green_posは(y,x)の順番なので、(x,y)に変換
cv2.circle(
    image_copy, tuple(green_center_pos[::-1]), 1, (0, 255, 0), 5
)  # (画像, 中心座標(y,x), 半径, 色(B,G,R), 線の太さ)

# 青色の座標に〇を描画 blue_posは(y,x)の順番なので、(x,y)に変換
cv2.circle(
    image_copy, tuple(blue_center_pos[::-1]), 1, (255, 0, 0), 5
)  # (画像, 中心座標(y,x), 半径, 色(B,G,R), 線の太さ)

# 　画像を保存
cv2.imwrite("output.jpg", image_copy)

# 画像を表示
cv2.imshow("image", image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
