import cv2 as cv
import numpy as np

src = cv.imread("Sobel_Operator/opencv.png")

h, w = src.shape[:2]

x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

cv.imshow("x_grad", x_grad)
cv.waitKey(1)

cv.imshow("y_grad", y_grad)
cv.waitKey(1)

dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)
cv.imshow("gradient", dst)
cv.waitKey(1)