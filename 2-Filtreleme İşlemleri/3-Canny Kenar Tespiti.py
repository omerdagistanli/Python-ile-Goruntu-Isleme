# Önce HSV formatına çeviriyoruz

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while (1):
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)            # hsv çevirme

    dusuk_mavi = np.array([100,60,60])
    ust_mavi = np.array([140,255,255])

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sonelX = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobelY = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # Canny
    kenarlar = cv2.Canny(frame, 100,200)                # eşik değerlerine göre kenar bulma olasılığı artıyor

    mask = cv2.inRange(hsv, dusuk_mavi, ust_mavi)     # ust ve alt sınırları belirleme
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow("Orjinal",frame)
    cv2.imshow("Canny", kenarlar)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()