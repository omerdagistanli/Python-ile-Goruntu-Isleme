import cv2
import numpy as np


mavi = [255, 0, 0]

img = cv2.imread("opencv.JPG")

replicate = cv2.copyMakeBorder(img, 10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10,10,10,10,cv2.BORDER_REFLECT)               # çerçeve kenarlarında yansıtma yaptı
reflect101 = cv2.copyMakeBorder(img, 10,10,10,10,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img, 10,10,10,10,cv2.BORDER_WRAP)                     # resmi desenmiş gibi gösterdi
constant = cv2.copyMakeBorder(img, 10,10,10,10,cv2.BORDER_CONSTANT, value=mavi) # çerçeve kenarını mavi yaptı

cv2.imshow("orjinal", img)
cv2.imshow("replicate", replicate)

cv2.waitKey(0)
cv2.destroyAllWindows()

