import cv2
import matplotlib.pyplot as plt


img_path = "C:\\Muhammad Raihan_1102224211\\Bagian 3\\Nomor 2\\yon.jpeg"
img_read = cv2.imread(img_path)


gray = cv2.colorChange(img_read, cv2.COLOR_BGR2GRAY)
(thresh, bnw) = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
cv2.imshow('Original', img_read)
cv2.imshow('Grayscale', gray)
cv2.imshow ('Black and White',bnw)

cv2.waitKey(0)
cv2.destroyAllWindows()

