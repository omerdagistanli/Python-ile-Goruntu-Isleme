import cv2
import numpy as np

img = cv2.imread("messi.jpg")
# print(img.item(100,100,0))                # x, y pikseline ait renk değerleri | 0 -> mavi, 1 -> yeşil 2 -> kırmızı
# img.itemset((5,5,1), 255)                 # x,y pikselini tam yeşil yaptık (gözüküyor)
# print(img.shape)                          # açılan çerçevenin (yüksekliği, genişliği, 3 renk)
# print(img.size)                           # resimdeki total pixel sayısı
# resimdekiTop = img[310:390, 272:330]
# img[310:390, 322:380] = resimdekiTop      # belirtilen alana topu yapıştırır  (değer aralıkları aynı olmalı)

# img[:, :, 0] = 0                          # mavi pixelleri 0 la
# img[:, :, 1] = 0                          # yeşil pixelleri 0 la
# img[:, :, 2] = 0                          # kırmızı pixelleri 0 la ve sonucunda siyah ekran :)

cv2.imshow("Resim",img)
# cv2.imshow("Top", resimdekiTop)
cv2.waitKey(0)
cv2.destroyAllWindows()