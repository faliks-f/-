import cv2

def planA(image):
    blur = cv2.blur(image, (3, 3))
    cv2.imshow("blur", blur)