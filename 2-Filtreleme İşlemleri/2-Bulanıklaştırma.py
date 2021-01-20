# Önce HSV formatına çeviriyoruz

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while (1):
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)            # hsv çevirme

    dusuk_mavi = np.array([100,60,60])
    ust_mavi = np.array([140,255,255])

    mask = cv2.inRange(hsv, dusuk_mavi, ust_mavi)     # ust ve alt sınırları belirleme
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15,15), np.float32) / 225
    smoothed = cv2.filter2D(son_resim, -1, kernel)

    # alternatif bulanıklaştırma
    blur = cv2.GaussianBlur(son_resim, (15,15), 0)

    cv2.imshow("Orjinal",frame)
    cv2.imshow("Son Resim", son_resim)
    cv2.imshow("smoothed", smoothed)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()