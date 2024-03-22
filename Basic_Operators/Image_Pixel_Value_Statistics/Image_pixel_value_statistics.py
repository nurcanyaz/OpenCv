#Performans Ölçme ve Geliştirme Teknikleri

import cv2 as cv
import numpy as np

path = "Basic_Operators/Image_Pixel_Value_Statistics/"
src = cv.imread(path + "opencv.png", cv.IMREAD_GRAYSCALE)

# Bir resmin min max değerine ve konumuna erişme
#MinMaxLoc

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min_values: %.2f, max_value: %.2f" % (min_value, max_value))
print("min loc:", min_loc, ",", "max loc:", max_loc)

#meanStdDev
means, stddev = cv.meanStdDev(src)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

src[np.where(src < means)] = 0
src[np.where(src > means)] = 255

cv.imshow("binary", src)
cv.waitKey(1)



