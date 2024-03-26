import cv2 as cv
import numpy as np

# Shifting
img = cv.imread("Geometric/car.jpg")
rows = img.shape[0]
cols = img.shape[1]

# warpAffine, bir görüntünün geometrik dönüşümlerini gerçekleştirmek için kullanılan bir işlevdir.


M = np.float32([[1, 0, 300], [0, 1, 90]])
shifted = cv.warpAffine(img, M, (cols, rows))
cv.imshow("original", img)
cv.waitKey(1)

cv.imshow("shifted", shifted)
cv.waitKey(1)

# rotation

M = cv.getRotationMatrix2D((cols/2, rows / 2), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow("img", dst)
cv.waitKey()

# Scaling
res = cv.resize(img, None, fx=0.2, fy=0.2,interpolation=cv.INTER_CUBIC)
cv.imshow("img", res)
cv.waitKey(1)

# kucuk resim
rows = res.shape[0]
cols = res.shape[1]

M = np.float32([[1, 0, 200], [0, 1, 90]])
shifted = cv.warpAffine(res, M, (cols, rows))
cv.imshow("original", res)
cv.waitKey(1)

shifted = cv.warpAffine(res, M, (cols, rows))
cv.imshow("shifted", shifted)
cv.waitKey(1)
