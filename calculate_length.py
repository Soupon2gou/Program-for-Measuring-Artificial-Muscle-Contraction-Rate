import cv2
import numpy as np
import sys
# 画像読み込み
image_path = ".\\resources\\hi_kukkyoku_color.jpg"  # 画像のパス
# image_path = "black.png"  # 画像のパス
image = cv2.imread(image_path)  # 画像の読み込み
if image is None:
    raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")

# calculate the length between the red and blue points
# 輪郭を抽出
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ����を求める
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# 輪郭を抽出
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# ����の長さを格��するリスト
lengths = []

# ����を表示
for i, contour in enumerate(contours):
    # ����の長さを求める
    length = cv2.arcLength(contour, True)
    lengths.append(length)
    # ����を描画
    cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)
    # ����の長さを表示
    cv2.putText(image, f"Length {i+1}: {length:.2f} pixels", (10, 30 + i*20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# ����の長さの平均を求める
average_length = np.mean(lengths)

# 平均長さを表示
cv2.putText(image, f"Average Length: {average_length:.2f} pixels", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# 画像を表示
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
