import cv2
import numpy as np

# 画像読み込み
image_path = "hi_kukkyoku_pattern.jpg"
start_template_path = "pattern_start.jpg"
end_template_path = "pattern_end.jpg"

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
start_template = cv2.imread(start_template_path, cv2.IMREAD_GRAYSCALE)
end_template = cv2.imread(end_template_path, cv2.IMREAD_GRAYSCALE)

#start_templateとend_templateの拡大率を71%にする
#t3 = cv2.resize(t2, (int(t2.shape[1]*i/100), int(t2.shape[0]*i/100)))
start_template_resized = cv2.resize(start_template, (int(start_template.shape[1]*71/100), int(start_template.shape[0]*71/100)))
end_template_resized = cv2.resize(end_template, (int(end_template.shape[1]*71/100), int(end_template.shape[0]*71/100)))

if image is None or start_template is None or end_template is None:
    raise FileNotFoundError("画像ファイルが見つかりません")

# テンプレートマッチングの手法
methods = {
    "SSD": cv2.TM_SQDIFF,
    "SAD": cv2.TM_SQDIFF_NORMED,
    "NCC": cv2.TM_CCORR_NORMED,
    "ZNCC": cv2.TM_CCOEFF_NORMED
}

# 結果を保存する辞書
results = {}

for method_name, method in methods.items():
    # テンプレートマッチング
    result_start = cv2.matchTemplate(image, start_template, method)
    result_end = cv2.matchTemplate(image, end_template, method)
    
    # 最も一致する位置を取得
    min_val_start, max_val_start, min_loc_start, max_loc_start = cv2.minMaxLoc(result_start)
    min_val_end, max_val_end, min_loc_end, max_loc_end = cv2.minMaxLoc(result_end)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        match_loc_start = min_loc_start
        match_loc_end = min_loc_end
        similarity_start = min_val_start
        similarity_end = min_val_end
    else:
        match_loc_start = max_loc_start
        match_loc_end = max_loc_end
        similarity_start = max_val_start
        similarity_end = max_val_end
    
    # テンプレートの中心位置を計算
    start_center = (match_loc_start[0] + start_template.shape[1] // 2, match_loc_start[1] + start_template.shape[0] // 2)
    end_center = (match_loc_end[0] + end_template.shape[1]// 2, match_loc_end[1] + end_template.shape[0] // 2)
    
    # 中心間の距離を計算
    distance = np.sqrt((start_center[0] - end_center[0]) ** 2 + (start_center[1] - end_center[1]) ** 2)
    
    # 結果を保存
    results[method_name] = {
        "start_center": start_center,
        "end_center": end_center,
        "similarity_start": similarity_start,
        "similarity_end": similarity_end,
        "distance": distance
    }

# 結果を表示
for method_name, result in results.items():
    print(f"{method_name} - 始点の中心: {result['start_center']}, 終点の中心: {result['end_center']}, 類似度（始点）: {result['similarity_start']}, 類似度（終点）: {result['similarity_end']}, 中心間の距離: {result['distance']}")

# 結果を画像に描画
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for method_name, result in results.items():
    start_center = result["start_center"]
    end_center = result["end_center"]
    #一致したテンプレートを描画
    cv2.rectangle(output_image, (start_center[0] - start_template.shape[1] // 2, start_center[1] - start_template.shape[0] // 2),
                  (start_center[0] + start_template.shape[1] // 2, start_center[1] + start_template.shape[0] // 2),
                  (0, 255, 0), 2)
    cv2.circle(output_image, start_center, 5, (0, 255, 0), -1)
    cv2.circle(output_image, end_center, 5, (0, 0, 255), -1)
    cv2.line(output_image, start_center, end_center, (255, 0, 0), 2)
    cv2.putText(output_image, method_name, (start_center[0] + 10, start_center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    

# 画像を表示
cv2.imshow("Result", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 始点と終点の色を変えてimgを表示
# if start_point:
#     for dy in range(-1, 2):
#         for dx in range(-1, 2):
#             y = start_point[1] + dy
#             x = start_point[0] + dx
#             if 0 <= y < img.shape[0] and 0 <= x < img.shape[1]:
#                 # 始点の周り9ピクセル
#                 img[y, x] = 127

# if end_point:
#     for dy in range(-1, 2):
#         for dx in range(-1, 2):
#             y = end_point[1] + dy
#             x = end_point[0] + dx
#             if 0 <= y < img.shape[0] and 0 <= x < img.shape[1]:
#                 img[y, x] = 127  # 終点の周り9ピクセル