import cv2


class ShapeDetector:
    def __init__(self):
        pass

    # 识别形状
    def detect(self, c):

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            shape = "Square"
        else:
            shape = "Circle"
        return shape
