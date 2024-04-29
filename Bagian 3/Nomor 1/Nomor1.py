import cv2
import matplotlib.pyplot as plt

img_path = "C:\Muhammad Raihan_1102224211\Bagian 3\Nomor 1\emma.jpg"
img_read = cv2.imread(img_path)

img_90 = cv2.flip(img_read,1)
img_180 = cv2.flip(img_read,0)
img_360 = cv2.transpose(img_read)

fig = plt.figure(figsize=(20,20))

ax1 = fig.add_subplot(1,5,1)
ax1.set_title("Normal")
ax1.imshow(img_read)
ax2 = fig.add_subplot(1,5,2)
ax2.set_title("Flip Horizontal")
ax2.imshow(img_90)
ax3 = fig.add_subplot(1,5,3)
ax3.set_title("Flip Vertical")
ax3.imshow(img_180)
ax4 = fig.add_subplot(1,5,4)
ax4.set_title("Transpose")
ax4.imshow(img_360)
plt.show()
