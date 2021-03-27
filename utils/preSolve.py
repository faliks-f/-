import cv2
import imutils
from utils.getMinRect import getSurroundRect
import numpy as np


def __countSquare(image, contour):
    mask = np.zeros(image.shape, dtype="uint8")
    mask = cv2.drawContours(mask, [contour], -1, 255, -1)
    mask = cv2.bitwise_and(image, image, mask=mask)
    # cv2.imshow("mask", mask)
    total = cv2.countNonZero(mask)
    return total


def preSolve(image, debugFlag):
    contourList = []
    roi = image
    blurred = cv2.GaussianBlur(roi, (1, 1), 0)
    lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for c in cnts:
        [point, width, height] = getSurroundRect(c)
        total = __countSquare(thresh, c)
        if debugFlag:
            cv2.drawContours(roi, [c], -1, (0, 255, 0), 2)
            cv2.imshow("roi", roi)
            cv2.waitKey(0)
            print(total)
            print(width, height)
            print("standard", width * height)
            # cv2.circle(image, (point[0], point[1]), 2, (0, 0, 255), -1)
            # print(width * height)
            # print(cv2.contourArea(c) / (width * height))
            # print(cv2.contourArea(c) > 250000)
        # print(height, width)
        if total < 1000:
            continue
        if total > 20000:
            continue
        if width / height < 0.9 or width / height > 1.1:
            continue
        # print(height, width)
        if total / (height * width) < 0.5:
            continue
        contourList.append(c)
    # print(len(contourList))
    return [roi, contourList, lab]
