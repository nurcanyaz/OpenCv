import cv2 as cv
import numpy as np

# Video okuma
capture = cv.VideoCapture("Basic_Operators/Video_Read_Write/video.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)

print(height, width, count, fps)

# Videoyu yazdırma

out = cv.VideoWriter("Basic_Operators/Video_Read_Write/new_video.avi",
                     cv.VideoWriter_fourcc('D','I','V','X'), 15,
                     (int(width), int(height)), True)

while True:
    # Kameradan görüntü al
    ret, frame = capture.read()
    # Görüntü başarıyla alındı mı kontrol et
    if ret is True:
        # Okunan görüntüyü ekranda göster.
        cv.imshow("video-input", frame)
        out.write(frame)
        # 50 sn sonra çık
        c = cv.waitKey(50)
        if c == 27: #ESC
            break
    else:
        break
# Videoyu kapatma
capture.release()
out.release()