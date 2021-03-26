import cv2
from utils.preSolve import preSolve
import _thread

debugFlag = False


def read_image(threadName):
    global image_
    while True:
        ret, image_ = capture.read()


image_ = None
capture = cv2.VideoCapture(1)

try:
    _thread.start_new_thread(read_image, ("1",))
except Exception as e:
    print("error")

while True:
    # ret, image = capture.read()
    if image_ is None:
        continue
    image = image_.copy()
    # image = cv2.imread("./1.jpg")
    preSolve(image, debugFlag)
    cv2.imshow("image", image)
    q = cv2.waitKey(1)
    if q == ord("d"):
        debugFlag = True
