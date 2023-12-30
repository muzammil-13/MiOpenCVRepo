import cv2

img=cv2.imread('lena.png',3)
print(img)
cv2.imshow('image',img)
cv2.waitKey(10000)