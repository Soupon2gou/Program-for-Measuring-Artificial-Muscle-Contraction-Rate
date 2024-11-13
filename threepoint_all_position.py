import numpy as np
import matplotlib.path as mpltPath

def enumerate_pixels_in_triangle(p1, p2, p3):
    # 3点から三角形の領域を計算
    triangle_points = np.array([p1, p2, p3])

    # 三角形の外接矩形を取得
    min_x = int(min(p1[0], p2[0], p3[0]))
    max_x = int(max(p1[0], p2[0], p3[0]))
    min_y = int(min(p1[1], p2[1], p3[1]))
    max_y = int(max(p1[1], p2[1], p3[1]))

    # 三角形の領域を判定するためのPathオブジェクトを作成
    path = mpltPath.Path(triangle_points)

    # 外接矩形内の全てのピクセルについて、三角形内かを判定
    pixels = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if path.contains_point((x, y)):
                pixels.append((x, y))
    
    return pixels

# 例: 座標 (10, 10), (20, 10), (15, 20) の3点が与えられた場合
p1 = (568, 0)
p2 = (909, 0)
p3 = (909, 59)
pixels = enumerate_pixels_in_triangle(p1, p2, p3)

print(pixels)
