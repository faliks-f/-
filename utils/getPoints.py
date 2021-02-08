import numpy as np


def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


# 获取点和长宽
def get_point_width_height(pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    widthA = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
    widthB = np.sqrt((tl[0] - tr[0]) ** 2 - (tl[1] - tr[1]) ** 2)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - tr[1]) ** 2)
    heightB = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    maxHeight = max(int(heightA), int(heightB))

    return [tl, maxWidth, maxHeight]
