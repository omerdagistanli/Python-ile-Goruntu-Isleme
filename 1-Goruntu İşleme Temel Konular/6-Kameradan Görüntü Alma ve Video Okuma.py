import cv2

kamera = cv2.VideoCapture(0)                # 0 -> webcam, 1 usb ile bağlı kamera

# kamera = cv2.VideoCapture("okuncakVideo.mp4")

while True:
    ret, goruntu = kamera.read()
    cv2.imshow("Goruntu", goruntu)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()