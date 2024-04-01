# IMAGE NOISE

import cv2 as cv
import numpy as np

src = cv.imread("Image_Noise/logo.png")

def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=np.int32)
    cols = np.random.randint(0, w, nums, dtype=np.int32)
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
    return  image

# Fonksiyona göndereceğimiz resmin boyutunu tutuyoruz.
h, w = src.shape[:2]

# Kopyasını alıyoruz.
copy = np.copy(src)
copy = add_salt_pepper_noise(copy)

# İki resmin yan yana gösterilmesini sağlıyoruz.
result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = copy

cv.imshow("Original and Copy with Noise",result)
cv.waitKey(1)
cv.destroyAllWindows()