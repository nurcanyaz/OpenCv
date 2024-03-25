# EŞİKLEME

import cv2 as cv

path = "Basic_Operators/Thresholding/"
src = cv.imread(path+ "work.jpg")

T = 127    # Eşik değeri

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# Range ile 5 tane resim oluşturduk.
for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)
cv.waitKey(1)
cv.destroyAllWindows()