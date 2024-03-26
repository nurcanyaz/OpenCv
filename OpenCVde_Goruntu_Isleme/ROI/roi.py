import cv2 as cv

src = cv.imread("ROI/car.jpg")
h, w = src.shape[:2]
img = src.copy()
roi = img[300:750, 950:1300, :]
roi.shape[:2]

cv.imshow("roi", roi)
cv.waitKey(1)

img[0:450, 0:350, :] = roi
cv.imshow("img", img)
cv.waitKey(1)

res = cv.resize(roi, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
cv.imshow("res", res)
cv.waitKey(1)

src[0:135, 0:105, :] = res
cv.imshow("img", src)
cv.waitKey(1)
