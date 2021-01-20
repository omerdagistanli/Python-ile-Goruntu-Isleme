import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("sudoku.JPG", 0)
resim = cv2.medianBlur(resim, 5)

ret, thresh1 = cv2.threshold(resim, 127,255,cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh3 = cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

basliklar = ["Org","Basit Thresholding(127)", "Mean C", "Gauss Mean C"]

resimler = [resim, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(resimler[i], "gray")
    plt.title(basliklar[i])
    plt.xticks([]), plt.yticks([])

plt.show()