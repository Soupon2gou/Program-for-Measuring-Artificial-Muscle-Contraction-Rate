import cv2
import numpy as np
def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey()
    cv2.destroyAllWindows()

# 画像読み込み
image_path = "hi_kukkyoku_pattern.jpg"
start_template_path = "pattern_start.jpg"

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
start_template = cv2.imread(start_template_path, cv2.IMREAD_GRAYSCALE)

if image is None or start_template is None:
    raise FileNotFoundError("画像ファイルが見つかりません")

ret_image = image.copy()
for i in range(60,80,1):
    t2 = start_template.copy()
    # 画像サイズを拡大
    t3 = cv2.resize(t2, (int(t2.shape[1]*i/100), int(t2.shape[0]*i/100)))
    result = cv2.matchTemplate(ret_image, t3, cv2.TM_CCOEFF_NORMED)
    # 最も一致する位置を取得
    loc = np.where(result > 0.6)
    w, h = t3.shape
    for pt in zip(*loc[::-1]):
        ret_image = cv2.rectangle(ret_image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        print(pt,",拡大率:",i)

# 画像を表示,画像のテンプレートが一致した位置に赤い四角を描画
show_image("Result", ret_image)
