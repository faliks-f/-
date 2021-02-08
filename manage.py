import cv2
from utils.getRoi import *

image = cv2.imread("./1.jpg")
roi = get_roi(image)
# cv2.imshow("roi", roi)
cv2.waitKey(0)
