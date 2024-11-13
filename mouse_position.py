import cv2
# print(cv2)


########################################################################
## マウス処理
def onMouse(event, x, y, flag, params):
    raw_img = params["img"]
    wname = params["wname"]
    point_list = params["point_list"]
    point_num = params["point_num"]
    
    ## クリックイベント
    ### 左クリックでポイント追加
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(point_list) < point_num:
            point_list.append([x, y])
    
    ### 右クリックでポイント削除
    if event == cv2.EVENT_RBUTTONDOWN:
        if len(point_list) > 0:
            point_list.pop(-1)

    ## レーダーの作成, 描画
    img = raw_img.copy()
    h, w = img.shape[0], img.shape[1]
    cv2.line(img, (x, 0), (x, h), (255, 0, 0), 1)
    cv2.line(img, (0, y), (w, y), (255, 0, 0), 1)

    ## 点, 線の描画
    for i in range(len(point_list)):
        cv2.circle(img, (point_list[i][0], point_list[i][1]), 3, (0, 0, 255), 3)
        if 0 < i:
            cv2.line(img, (point_list[i][0], point_list[i][1]),
                     (point_list[i-1][0], point_list[i-1][1]), (0, 255, 0), 2)
        if i == point_num-1:
            cv2.line(img, (point_list[i][0], point_list[i][1]),
                     (point_list[0][0], point_list[0][1]), (0, 255, 0), 2)
    
    if 0 < len(point_list) < point_num:
        cv2.line(img, (x, y),
                     (point_list[len(point_list)-1][0], point_list[len(point_list)-1][1]), (0, 255, 0), 2)
    
    ## 座標情報をテキストで出力
    cv2.putText(img, "({0}, {1})".format(x, y), (0, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow(wname, img)


## 取得した座標情報を保存
def save_point_list(path, point_list):
    f = open(path, "w")
    for p in point_list:
        f.write(str(p[0]) + "," + str(p[1]) + "\n")
    f.close()


def main():
    # 画像読み込み
    img_path = "hi_kukkyoku.jpg"  # 画像のパス
    # img_path = "black.png"  # 画像のパス
    img = cv2.imread(img_path)  # 画像の読み込み
    #画像の解像度をHHDに変更
    img = cv2.resize(img, dsize=(1920, 1080))
    if img is None:
        raise FileNotFoundError(f"画像ファイルが見つかりません: {img_path}")
    # 画像のトリミング
    trimmed_img = img[400:460, 490:1400]
    trimmed_img_width = trimmed_img.shape[1]

    ## 諸々設定
    wname = "MouseEvent"
    point_list = []
    point_num = 4 #今回は矩形がほしかったので4
    params = {
        "img": trimmed_img,
        "wname": wname,
        "point_list": point_list,
        "point_num": point_num,
    }

    ## メイン
    cv2.namedWindow(wname)
    cv2.setMouseCallback(wname, onMouse, params)
    cv2.imshow(wname, trimmed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ## 取得したポイントに囲まれたピクセルを全列挙してリストにする、そしてそれをprintする
    mask = cv2.inRange(trimmed_img, (0, 0, 0), (0, 0, 0))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    pixel_list = []
    for cnt in contours:
        for p in cnt:
            x, y = p[0][0], p[0][1]
            pixel_list.append((x, y))
    print(pixel_list)
    

if __name__ == "__main__":
    main()