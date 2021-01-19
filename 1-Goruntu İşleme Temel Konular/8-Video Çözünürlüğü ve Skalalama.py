import cv2

kamera = cv2.VideoCapture(0)

def cozunurluk_1366():
    kamera.set(3,1366)
    kamera.set(4,768)

def cozunurluk_720():
    kamera.set(3,1280)
    kamera.set(4,720)

def cozunurluk_480():
    kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def cozunurluk_belirle(width, height):
    kamera.set(3, width)
    kamera.set(4, height)

# cozunurluk_480()
# cozunurluk_720()
# cozunurluk_1366()
cozunurluk_belirle(1000,100)

def scalalama(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    boyut = (width, height)

    return cv2.resize(frame, boyut, interpolation=cv2.INTER_AREA)

while True:
    ret, frame = kamera.read()
    frame75 = scalalama(frame, 75)
    cv2.imshow("Goruntu", frame)
    cv2.imshow("Goruntu2", frame75)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()