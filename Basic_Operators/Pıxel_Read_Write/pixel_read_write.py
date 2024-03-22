import cv2 as cv

path = "Basic_Operators/Pıxel_Read_Write/"
img = cv.imread(path + "opencv.png")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.destroyAllWindows()
