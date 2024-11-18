import cv2
import numpy as np


def find_red_and_blue(image):
    # RGBからHSVに変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    ########################################################################
    # imageにおいて赤色を全探索して、その座標を取得する
    # 赤色の閾値を設定
    lower_red1 = np.array([0, 100, 100])  # 下限 (色相, 彩度, 明度)
    upper_red1 = np.array([10, 255, 255])  # 上限

    # 赤色の部分をimageから取得
    mask = cv2.inRange(image, lower_red1, upper_red1)
    # 赤色の部分をimageから取得
    red = cv2.bitwise_and(
        image, image, mask=mask
    )  # bitwise_and(元画像, 元画像, マスク画像)
    # 赤色の部分の位置を取得
    red_pos = np.where(mask == 255)

    ########################################################################

    # 青色の部分を全探索して、その座標を取得する
    # 青色の閾値を設定
    lower_blue1 = np.array([100, 80, 40])  # 下限 (色相, 彩度, 明度)
    upper_blue1 = np.array([130, 255, 255])  # 上限

    # 青色の部分をimageから取得
    mask = cv2.inRange(image, lower_blue1, upper_blue1)

    # 青色の部分をimageから取得
    blue = cv2.bitwise_and(image, image, mask=mask)

    # 青色の部分の位置を取得
    blue_pos = np.where(mask == 255)

    return red_pos, blue_pos
