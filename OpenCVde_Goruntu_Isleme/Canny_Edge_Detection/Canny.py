import cv2 as cv
import numpy as np

src = cv.imread("Canny_Edge_Detection/rose.jpg")
cv.imshow("rose", src)
cv.waitKey(1)


# Canny kenar algılama algoritmasını uygula
edge = cv.Canny(src, 100, 300)
cv.imshow("mask image", edge)
cv.waitKey(1)

# Burada yine Canny uygulandı ancak foto gri tonlamalı hale getirilip
# gürültü azaltıldığı için ortaya daha iyi bir sonuç çıktı.

# Gri tonlamalı hale getir
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için Gauss filtresi uygula
blur = cv.GaussianBlur(gray, (5, 5), 0)

# Canny kenar algılama algoritmasını uygula
edges = cv.Canny(blur, 50, 150)

# Sonuçları görselleştir
cv.imshow('Original Image', src)
cv.imshow('Canny Edges', edges)
cv.waitKey(0)
cv.destroyAllWindows()