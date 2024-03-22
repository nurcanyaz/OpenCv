
import cv2 as cv

path = "Basic_Operators/Load_Image/"
img = cv.imread(path + "image.jpg")

type(img)

#namedWindow
# Resmin ismini okuduktan sonra bir pencerede tutmaya yarar.
# Yazdığımız ilk string ifade açılan pencerenin adı olur.
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

#imshow
cv.imshow("opencv_test", img)
cv.waitKey(1)
# Burada 1 yerine 0 yazarsak bu işlem sonsuza kadar aktif tutulur.
# Pozitif sayı girersek milisaniye cinsinden ne kadar açık tutulacağı bilgisi bulunmmuş olur.

# Açık olan pencerelerin kapatılmasını sağlar.
cv.destroyAllWindows()