import cv2 as cv

path = "Basic_Operators/Load_Image/"
img = cv.imread(path + "image.jpg")
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

# Resimdeki beyaz yerleri siyah yapma

h, w, ch = img.shape
print("h, w, ch", h, w, ch)

for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = [b, g, r]

cv.imshow("output", img)
cv.waitKey(1)
