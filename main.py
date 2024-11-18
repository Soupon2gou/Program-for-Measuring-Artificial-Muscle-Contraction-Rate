import cv2
import numpy as np
import sys
from find_start_end import find_start_end
from calculate_length import calculate_length

# 画像読み込み
image_path = ".\\resources\\hi_kukkyoku_color.jpg"  # 画像のパス
# image_path = "black.png"  # 画像のパス
image = cv2.imread(image_path)  # 画像の読み込み
if image is None:
    raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
# 画像のコピー
image_copy = image.copy()
################################################################
# メイン処理
# find_start_end.pyよりred_posとblue_posを取得
red_pos, blue_pos = find_start_end(image)

# 赤色の中心座標を取得
red_center_pos = np.array([int(red_pos[0].mean()), int(red_pos[1].mean())])

# 青色の中心座標を取得
blue_center_pos = np.array([int(blue_pos[0][0].mean()), int(blue_pos[1][0].mean())])

# 長さを計算
length = calculate_length(red_center_pos, blue_center_pos, image)
print(f"length: {length}")
################################################################
# 描画と表示
# 赤色の座標に〇を描画 red_posは(y,x)の順番なので、(x,y)に変換
cv2.circle(
    image_copy, tuple(red_center_pos[::-1]), 1, (0, 0, 255), 5
)  # (画像, 中心座標(y,x), 半径, 色(B,G,R), 線の太さ)

# 青色の座標に〇を描画 blue_posは(y,x)の順番なので、(x,y)に変換
cv2.circle(
    image_copy, tuple(blue_center_pos[::-1]), 1, (255, 0, 0), 5
)  # (画像, 中心座標(y,x), 半径, 色(B,G,R), 線の太さ)

# 画像を保存
# cv2.imwrite("output.jpg", image_copy)
# 画像を表示
# cv2.imshow("image", image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
