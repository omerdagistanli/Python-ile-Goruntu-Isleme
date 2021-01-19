import cv2
img = cv2.imread("saat.jpg")

cv2.imshow("saat", img)

cv2.rectangle(img,(95,25),(208,120), (0,255,255),2)

cv2.imshow("saat2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()