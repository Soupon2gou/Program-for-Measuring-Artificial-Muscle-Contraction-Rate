import cv2
import numpy as np


def find_point(image):
    # RGBからHSVに変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # red_posとgreen_posとblue_posの初期値を設定
    red_pos = [0, 0]
    green_pos = [0, 0]
    blue_pos = [0, 0]

    ########################################################################
    # imageにおいて赤色を全探索して、その座標を取得する
    # 赤色の閾値を設定
    lower_red = np.array([0, 100, 100])  # 下限 (色相, 彩度, 明度)
    upper_red = np.array([10, 255, 255])  # 上限

    # 赤色の部分をimageから取得
    mask = cv2.inRange(image, lower_red, upper_red)
    # 赤色の部分をimageから取得
    red = cv2.bitwise_and(
        image, image, mask=mask
    )  # bitwise_and(元画像, 元画像, マスク画像)
    # 赤色の部分の位置を取得
    red_pos = np.where(mask == 255)

    ########################################################################

    # 青色の部分を全探索して、その座標を取得する
    # 青色の閾値を設定
    lower_blue = np.array([100, 80, 40])  # 下限 (色相, 彩度, 明度)
    upper_blue = np.array([130, 255, 255])  # 上限

    # 青色の部分をimageから取得
    mask = cv2.inRange(image, lower_blue, upper_blue)

    # 青色の部分をimageから取得
    blue = cv2.bitwise_and(image, image, mask=mask)

    # 青色の部分の位置を取得
    blue_pos = np.where(mask == 255)

    ########################################################################

    # 緑色の部分を全探索して、その座標を取得する
    # 緑色の閾値を設定
    lower_green = np.array([40, 80, 40])  # 下限 (色相, 彩度, 明度)
    upper_green = np.array([70, 255, 255])  # 上限
    # 緑色の部分をimageから取得
    mask = cv2.inRange(image, lower_green, upper_green)
    # 緑色の部分をimageから取得
    green = cv2.bitwise_and(image, image, mask=mask)
    # 緑色の部分の位置を取得
    green_pos = np.where(mask == 255)

    ########################################################################
    # 赤色の部分の位置をimageに描画
    image[red_pos[0], red_pos[1]] = [0, 0, 255]

    # 青色の部分の位置をimageに描画
    image[blue_pos[0], blue_pos[1]] = [255, 0, 0]

    # 緑色の部分の位置をimageに描画
    image[green_pos[0], green_pos[1]] = [0, 255, 0]

    # 赤色の中心座標を取得
    red_center_pos = np.array([int(red_pos[0].mean()), int(red_pos[1].mean())])

    # 青色の中心座標を取得
    blue_center_pos = np.array([int(blue_pos[0][0].mean()), int(blue_pos[1][0].mean())])

    # 緑色の中心座標を取得
    green_center_pos = np.array(
        [int(green_pos[0][0].mean()), int(green_pos[1][0].mean())]
    )

    return red_center_pos, green_center_pos, blue_center_pos
