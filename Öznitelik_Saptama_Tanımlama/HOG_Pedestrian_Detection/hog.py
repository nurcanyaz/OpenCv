# HOG

import cv2
import numpy as np

src = cv2.imread("HOG_Pedestrian_Detection/yaya.jpg")
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(src,
                                      winStride=(4, 4),
                                      padding=(8, 8),
                                      scale=1.5)

for (x, y, w, h) in rects:
    cv2.rectangle(src, (x, y), (x + w, y + h), (0, 25, 0), 2)

cv2.imshow("hog_detection", src)
cv2.waitKey(1)