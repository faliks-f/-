import cv2
from utils.getInformation import *
from utils.usart import *

moveThresh = 10


def __move(roi, cX, cY, completeFlag):
    [width, height] = roi.shape[:2]
    if (cX - width / 2) < moveThresh:
        serial_encoder("Left")
        return
    elif (cX - width / 2) > moveThresh:
        serial_encoder("Right")
        return
    if (cY - height / 2) < moveThresh:
        serial_encoder("Down")
        return
    elif (cY - height / 2) > moveThresh:
        serial_encoder("Up")
        return
    completeFlag = True


def task1(roi, lab, cnts, debugFlag, completeFlag):
    if len(cnts) > 1:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    c = cnts[0]
    [shape, color] = getColorAndShapeInformation(lab, c)
    [cX, cY] = getCenterInformation(c)
    drawDebugInformation(roi, c, color, shape, cX, cY)


def task3(roi, lab, cnts, debugFlag, completeFlag):
    if len(cnts) > 1:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    c = cnts[0]
    [shape, color] = getColorAndShapeInformation(lab, c)
    [cX, cY] = getCenterInformation(c)
    drawDebugInformation(roi, c, color, shape, cX, cY)
    __move(roi, cX, cY, completeFlag)


def task4(roi, lab, cnts, standardShape, standardColor, debugFlag, completeFlag):
    for c in cnts:
        [shape, color] = getColorAndShapeInformation(lab, c)
        if shape == standardShape or color == standardColor:
            [cX, cY] = getCenterInformation(c)
            __move(cX, cY, roi, completeFlag)


def task5(roi, lab, cnts, whichOne, debugFlag, completeFlag):
    shapeAndColor = []
    twoContours = []
    for c in cnts:
        [shape, color] = getColorAndShapeInformation(lab, c)
        shapeAndColor.append([shape, color, c])

    for i in range(len(shapeAndColor)):
        flag = False
        for j in range(i + 1, len(shapeAndColor)):
            if shapeAndColor[i][0] == shapeAndColor[j][0] and shapeAndColor[i][1] == shapeAndColor[j][1]:
                twoContours.append(shapeAndColor[i][2])
                twoContours.append(shapeAndColor[j][2])
                flag = True
                break
        if flag:
            break

    points = []
    if len(twoContours) > 0:
        for c in twoContours:
            [cX, cY] = getCenterInformation(c)
            drawDebugInformation(roi, c, color, shape, cX, cY)
            points.append([cX, cY])

    if len(points) > 0:
        first = points[0]
        second = points[1]
        if first[0] > second[0]:
            points = [second, first]
        elif first[0] == second[0]:
            if first[1] > second[1]:
                points = [second, first]

    if whichOne == "LeftAndUp":
        __move(roi, points[0][0], points[0][1], completeFlag)
    else:
        __move(roi, points[1][0], points[1][1], completeFlag)

    if completeFlag == True and whichOne == "LeftAndUp":
        completeFlag = False
        whichOne = "RightAndDown"
