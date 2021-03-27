from utils.preSolve import preSolve
from task import *
from utils.usart import *
import _thread

debugFlag = False
p = None
standardShape = None
standardColor = None
result = None
image_ = None
capture = cv2.VideoCapture(1)
completeFlag = True
whichOne = "LeftAndUp"

openSerial()


def read_image(threadName):
    global image_
    while True:
        ret, image_ = capture.read()


try:
    _thread.start_new_thread(read_image, ("1",))
except Exception as e:
    print("error")

while True:
    # ret, image = capture.read()
    if image_ is None:
        continue

    image = cv2.imread("./1.jpg")
    # image = image_.copy()
    [roi, contourList, lab] = preSolve(image, debugFlag)
    if completeFlag:
        result = serial_decoder()
        whichOne = "LeftAndUp"
    if result is not None:
        if result[0] == "P1":
            task1(roi, lab, contourList, debugFlag, completeFlag)
        elif result[0] == "P3":
            task3(roi, lab, contourList, debugFlag, completeFlag)
        elif result[0] == "P4":
            task4(roi, lab, contourList, result[1], result[2], debugFlag, completeFlag)
        elif result[0] == "P5":
            task5(roi, lab, contourList, whichOne, debugFlag, completeFlag)
    cv2.imshow("image", image)
    q = cv2.waitKey(1)
    if q == ord("d"):
        debugFlag = True
