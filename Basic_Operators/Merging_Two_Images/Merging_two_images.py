import cv2 as cv
import numpy as np

path = "Basic_Operators/Merging_Two_Images/"

img1 = cv.imread(path + "right.jpg")
img2 = cv.imread(path + "left.jpg")

cv.imshow("spiderman1", img1)
cv.waitKey(1)

cv.imshow("spiderman2", img2)
cv.waitKey(1)

horizontal = np.hstack((img2, img1))
cv.imshow("spider_man", horizontal)
cv.waitKey(1)