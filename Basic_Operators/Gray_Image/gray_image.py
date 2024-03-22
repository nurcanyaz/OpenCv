# GRAY IMAGE

import cv2 as cv
path = "Basic_Operators/Gray_Image/"

img = cv.imread(path + "opencv.png")
cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.imshow("colored", img)
cv.waitKey(1)

# cvtColor: Resmin formatını değiştirmek için kullanırız.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)
cv.destroyAllWindows()

# Gri görseli kaydetme
#imwrite

cv.imwrite(path + "gray_opencv.png", gray)
cv.destroyAllWindows()