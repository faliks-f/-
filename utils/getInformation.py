import cv2

from utils.shapeDetect import ShapeDetector
from utils.colorDetect import ColorLabeler


def getColorAndShapeInformation(lab, c):
    shapeDetector = ShapeDetector()
    colorLabeler = ColorLabeler()
    shape = shapeDetector.detect(c)
    color = colorLabeler.label(lab, c)
    return [shape, color]


def getCenterInformation(c):
    M = cv2.moments(c)
    if M["m00"] == 0:
        return False
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    return [cX, cY]


def drawDebugInformation(roi, c, color, shape, cX, cY):
    text = "{} {}".format(color, shape)
    cv2.drawContours(roi, [c], -1, (0, 255, 0), 2)
    cv2.putText(roi, text, (cX, cY),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
