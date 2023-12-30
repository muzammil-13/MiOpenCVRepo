import cv2
image=cv2.imread('blue.jpg',1)
new_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('hsvimage',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()