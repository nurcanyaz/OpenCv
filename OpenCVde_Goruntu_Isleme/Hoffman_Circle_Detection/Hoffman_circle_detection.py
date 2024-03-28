import cv2 as cv
import numpy as np

# Görüntüyü yükle
src = cv.imread("Hoffman_Circle_Detection/circle.jpg")

# Gri tonlamaya dönüştür
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
gray_blurred = cv.GaussianBlur(gray, (9, 9), 2, 2)

# Hough Circle tespiti için parametreleri ayarla ve daireleri bul
circles = cv.HoughCircles(gray_blurred, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30,
                          minRadius=20, maxRadius=100)

# Eğer daireler tespit edildiyse
if circles is not None:
    circles = np.uint16(np.around(circles))
    for c in circles[0, :]:
        # Dairenin merkez koordinatlarını ve yarıçapını al
        cx, cy, r = c
        # Merkezi noktayı ve daireyi çiz
        cv.circle(src, (cx, cy), 2, (0, 255, 0), 2)
        cv.circle(src, (cx, cy), r, (0, 0, 255), 2)

    # Sonucu göster
    cv.imshow("Hoffman Circle Detection", src)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Daire bulunamadı.")
