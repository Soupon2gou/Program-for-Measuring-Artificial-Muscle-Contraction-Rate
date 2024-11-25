import cv2
import numpy as np
import sys


def calculate_length(red_center_pos, green_center_pos, blue_center_pos, image):
    hik_length = 0
    k_length = 0

    # hik_lengthは赤色と青色の中心座標のユークリッド距離
    hik_length = np.linalg.norm(red_center_pos - blue_center_pos)

    # K_lengthは赤色と緑色の中心座標のユークリッド距離と青色と緑色の中心座標のユークリッド距離の和
    k_length = np.linalg.norm(red_center_pos - green_center_pos) + np.linalg.norm(
        blue_center_pos - green_center_pos
    )

    return hik_length, k_length
