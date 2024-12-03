import cv2
import numpy as np
import matplotlib.pyplot as plt
from find_point import find_point
from calculate_length import calculate_length

# 動画読み込み
video_path = ".\\resources\\zikken.MOV"  # 動画のパス
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise FileNotFoundError(f"動画ファイルが見つかりません: {video_path}")

# 収縮率と時間を保存するリスト
shrink_rates = []
times = []

# フレームレートを取得
fps = cap.get(cv2.CAP_PROP_FPS)

# フレームごとに処理
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # メイン処理
    try:
        red_center_pos, green_center_pos, blue_center_pos = find_point(frame)
        hik_length, k_length = calculate_length(
            red_center_pos, green_center_pos, blue_center_pos, frame
        )

        # 収縮率計算
        shrink_rate = 1.0 - (k_length / hik_length)
        shrink_rate *= 100  # 百分率に変換

        # 時間を計算
        time = frame_count / fps

        # 収縮率と時間を保存
        shrink_rates.append(shrink_rate)
        times.append(time)

        # フレームに描画
        red_center_pos = tuple(map(int, red_center_pos))
        green_center_pos = tuple(map(int, green_center_pos))
        blue_center_pos = tuple(map(int, blue_center_pos))
        cv2.circle(frame, red_center_pos[::-1], 1, (0, 0, 255), 5)
        cv2.circle(frame, green_center_pos[::-1], 1, (0, 255, 0), 5)
        cv2.circle(frame, blue_center_pos[::-1], 1, (255, 0, 0), 5)

        # フレームを表示
        # cv2.imshow("Frame", frame)
        # if cv2.waitKey(1) & 0xFF == ord("q"):
        #     break

    except ValueError as e:
        print(e)

    frame_count += 1

# 動画を解放
cap.release()
cv2.destroyAllWindows()

# グラフを作成
plt.plot(times, shrink_rates, label="収縮率")
plt.xlabel("時間 (秒)")
plt.ylabel("収縮率 (%)")
plt.title("時間と収縮率の関係")
plt.legend()
plt.show()

print("処理が終了しました")  # 処理が終了したことを表示
