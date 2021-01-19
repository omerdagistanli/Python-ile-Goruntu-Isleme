import cv2

kamera = cv2.VideoCapture(0)                    # 0 -> webcam, 1 usb ile bağlı kamera
# kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)       # GENİŞLİK
# kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)      # YUKSEKLİK

# Alternatif
kamera.set(3,360)
kamera.set(4,240)


while True:
    ret, goruntu = kamera.read()
    gri = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Goruntu", goruntu)
    cv2.imshow("Gri Ton", gri)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()