##########################################
# NESNE TESPİTİ: OPENCV TEMPLATE MATCHING
##########################################

import cv2 as cv
import numpy as np

path = "Template_Matching"

def template_demo():
    src = cv.imread(path + "/2.jpg")
    tpl = cv.imread(path + "/1.jpg")

    cv.imshow("input", src)
    cv.imshow("tpl", tpl)

    th, tw = tpl.shape[:2]

    result = cv.matchTemplate(src, tpl, method=cv.TM_CCORR_NORMED)
    cv.imshow("result", result)

    t = 0.98
    loc = np.where(result > t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0)
    cv.imshow("ilk_demo", src)
template_demo()
cv.waitKey(1)