import cv2 as cv

# HSV
# Hsv: Renk tonu, doygunluk ve değer olarak bilinir. Rgb renk uzayından farklı bir renk temsili sunar.

img = cv.imread("Changing_colorspace/car.jpg")
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", img)
cv.waitKey(1)

# RGB to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(1)
