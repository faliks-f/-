import cv2
from tasks.task1 import task1

image = cv2.imread("./1.jpg")
roi = task1(image)
# cv2.waitKey(0)
