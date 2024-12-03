import cv2
import numpy as np


# 　マウスクリックした座標のHSV値を取得する関数
def get_hsv_value(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_value = hsv_image[y, x]
        print(f"HSV Value at ({x}, {y}): {hsv_value}")


# Load the image
image_path = ".\\resources\\hi_kukkyoku_color2.jpg"  # 画像のパス
image = cv2.imread(image_path)

# Convert the image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# マウスクリックした座標のHSV値を取得するためのウィンドウを作成
cv2.namedWindow("HSV Image")
cv2.setMouseCallback("HSV Image", get_hsv_value)

while True:
    # Display the HSV image
    cv2.imshow("HSV Image", hsv_image)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Destroy all windows
cv2.destroyAllWindows()
