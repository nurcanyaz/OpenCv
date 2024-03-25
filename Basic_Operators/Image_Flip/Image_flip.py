import cv2 as cv
import numpy as np

path = "Basic_Operators/Image_Flip/"
src = cv.imread(path + "opencv.png")
# Flip: iki boyutlu bir dizi eksenler arasında döndürmeyi içerir.

# X Flip
# FlipCode 0 olduğunda x eksenine göre çevirme yapar.

dst1 = cv.flip(src,0)
cv.imshow("x-flip", dst1)
cv.waitKey(1)

# Y Flip
# FlipCode 1 olduğunda y eksenine göre çevirme yapar.

dst2 = cv.flip(src,1)
cv.imshow("y-flip", dst2)
cv.waitKey(1)

# XY Flip
# FlipCode -1 olduğunda hem x hem de y eksenine göre çevirme yapar.
dst3 = cv.flip(src, -1)
cv.imshow("xy-flip", dst3)
cv.waitKey(1)