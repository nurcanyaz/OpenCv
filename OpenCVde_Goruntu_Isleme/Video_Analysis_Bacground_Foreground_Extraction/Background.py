import cv2 as cv

# Video dosyasını aç
cap = cv.VideoCapture("Video_Analysis_Bacground_Foreground_Extraction/video.mp4")

# Arka plan çıkartıcı nesnesini oluştur
fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=500)

while True:
    # Videodan bir kare al
    ret, frame = cap.read()

    # Arka plan çıkartma işlemi uygula
    fgmask = fgbg.apply(frame)

    # Arka plan görüntüsünü al
    background = fgbg.getBackgroundImage()

    # Görüntüleri göster
    cv.imshow("input", frame)
    cv.imshow("mask", fgmask)
    cv.imshow("background", background)

    # Çıkış için klavyeden ESC tuşuna basmayı bekle
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

# Video işlemleri tamamlandığında kapat
cap.release()
cv.destroyAllWindows()
