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

    # imageにhik_lengthを測った長さを描画
    cv2.line(
        image,
        tuple(red_center_pos[::-1]),
        tuple(blue_center_pos[::-1]),
        (0, 0, 255),
        2,
    )
    # imageにk_lengthを測った長さを描画
    cv2.line(
        image,
        tuple(red_center_pos[::-1]),
        tuple(green_center_pos[::-1]),
        (0, 255, 0),
        2,
    )
    # imageにK_lengthを測った長さを描画
    cv2.line(
        image,
        tuple(blue_center_pos[::-1]),
        tuple(green_center_pos[::-1]),
        (255, 0, 0),
        2,
    )
    # 画像を保存
    cv2.imwrite("output_length.jpg", image)

    # 画像を表示
    cv2.imshow("image", image)
    cv2.waitKey(0)

    return hik_length, k_length
