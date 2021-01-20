import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("messi.jpg",0)
kenarlar = cv2.Canny(resim, 100,200)

plt.subplot(121),plt.imshow(resim, cmap="gray")
plt.title("Orjinal"),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(kenarlar, cmap="gray")
plt.title("Kenarlar"),plt.xticks([]),plt.yticks([])

plt.show()