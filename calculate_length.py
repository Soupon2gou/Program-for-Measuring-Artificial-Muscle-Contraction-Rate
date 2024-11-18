import cv2
import numpy as np
import sys


def calculate_length(red_center_pos, blue_center_pos, image):
    length = 0
    # 画像の輪郭を取得して、その輪郭の長さを計算
    # 画像をグレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 2値化
    _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    # 輪郭を取得
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # ����の長さを計算
    for cnt in contours:
        length += cv2.arcLength(cnt, True)

    # ��色と青色の中心間の距��を計算
    distance = np.linalg.norm(np.array(red_center_pos) - np.array(blue_center_pos))

    return length, distance
