import cv2
import imutils
from utils.getPoints import get_point_width_height


def get_roi(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    edged = cv2.Canny(blurred, 75, 200)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    roi = None

    if len(cnts) > 0:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx == 4):
                [point, width, height] = get_point_width_height(approx.reshape(4, 2))
                r = float(width) / float(height)
                if r > 0.9 and r < 1.1:
                    roi = approx
                    break
            cv2.waitKey(0)
        [point, width, height] = get_point_width_height(roi.reshape(4, 2))
        x, y = int(point[0]), int(point[1])
        roi = image[y: y + height, x: x + width]
        # roi = roi.copy()
    return [roi, point, width, height]
