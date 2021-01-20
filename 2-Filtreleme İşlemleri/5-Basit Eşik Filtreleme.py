import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("gradient.JPG")

ret, thresh1 = cv2.threshold(resim, 127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(resim, 127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(resim, 127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(resim, 127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(resim, 127,255,cv2.THRESH_TOZERO_INV)

basliklar = ["orjinal", "Bınary", "bınary_ınv","trunc","tozero","tozero_ınv"]

resimler = [resim, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i], "gray")
    plt.title(basliklar[i])
    plt.xticks([]), plt.yticks([])

plt.show()