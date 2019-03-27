import numpy as np
import cv2


cv2.waitKey(10000)

cap = cv2.VideoCapture(0)
while(1):

    # Take each frame
    _, frame = cap.read()

    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(image, contours, -1, (0,255,0), 3)
    cv2.imshow('img',img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()