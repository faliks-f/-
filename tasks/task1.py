import cv2
import imutils
from utils.getRoi import get_roi
from utils.shapeDetect import ShapeDetector
from utils.colorDetect import ColorLabeler
from utils.usart import move
from utils.usart import sendColorAndShape


def task1(image):
    [roi, point, width, height] = get_roi(image)
    blurred = cv2.GaussianBlur(roi, (3, 3), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
    thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    print(len(cnts))
    c = cnts[0]
    sd = ShapeDetector()
    cl = ColorLabeler()
    shape = sd.detect(c)
    color = cl.label(lab, c)

    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    text = "{} {}".format(color, shape)

    cv2.drawContours(roi, [c], -1, (0, 255, 0), 2)
    cv2.putText(roi, text, (cX, cY),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.imshow("image", image)
    cv2.imshow("roi", roi)
    cv2.waitKey(0)
    # 此处发送颜色和形状，注意只发送一次
    from commonVariable import isSend
    global isSend
    if not isSend:
        sendColorAndShape(color, shape)
        isSend = True
    # 图形在原图中的中心点位置
    centerX, centerY = cX + int(point[0]), cY + int(point[1])
    return move(centerX, centerY)
