import cv2

img = cv2.imread("sayfa.jpg")
ret, th = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thgri = cv2.threshold(griton, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(griton, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("Org", img)
cv2.imshow("Th", th)
cv2.imshow("THgri", thgri)
cv2.imshow("Gaus", gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()