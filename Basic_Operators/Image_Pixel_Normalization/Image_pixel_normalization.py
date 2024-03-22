# IMAGE PIXEL NORMALIZATION
# Elimize aldığımız resimlerin temsil şekillerini normalize ediyor olucaz.
# Resmin ana özelliklerini kkoruyup gösterim şekillerini değiştiriyoruz.
import cv2 as cv
import numpy as np

path = "Basic_Operators/Image_Pixel_Normalization/"
src = cv.imread(path + "opencv.png")
print(src.shape)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)
print(gray.shape)  # rgb değeri kalktı.
print(gray)

# Standartlaştırma işlemleri için integer form kullanışlı olmadığı için floata çevirdik.
gray = np.float32(gray)
print(gray)

#NORM_MINMAX
print(gray)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_values: %.2f, max_value: %.2f" % (min_value, max_value))

means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

dst = np.zeros(gray.shape, dtype=np.float32)

cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)

print(np.uint8(dst*255))

means, stddev = cv.meanStdDev(np.uint8(dst*255))
print("mean: %.2f, stddev: %.2f" % (means, stddev))

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1)

# NORM_INF
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_INF)
print(dst)
cv.imshow("NORM_INF", np.uint8(dst*255))
cv.waitKey(1)

# NORM_L1
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L1)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*10000000))
cv.waitKey(1)

# NORM_L2
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L2)
print(dst)
cv.imshow("NORM_L2", np.uint8(dst*10000))
cv.waitKey(1)

