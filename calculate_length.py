import cv2
import numpy as np
import sys
# 画像読み込み
image_path = ".\\resources\\hi_kukkyoku_color.jpg"  # 画像のパス
# image_path = "black.png"  # 画像のパス
image = cv2.imread(image_path)  # 画像の読み込み
if image is None:
    raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")