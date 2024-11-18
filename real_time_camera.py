import cv2

# print(cv2)

# cameraでリアルタイムに画像を取得する場合は、以下のコードを使う
cap = cv2.VideoCapture(0)

image = cv2.resize(cap, dsize=(1920, 1080))
