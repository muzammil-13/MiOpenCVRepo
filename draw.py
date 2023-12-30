import cv2
image=cv2.imread('lena.png',1)
# Line drawing
cv2.line(image,(0,0),(400,400),(255,0,0),5)
# Rectangle drawing
cv2.rectangle(image,(0,0),(400,400),(0,255,0),4)
# Circle drawing
cv2.circle(image,(200,200),100,(0,0,255),-1)
# Text adding
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,'Hello',(100,100),font,2,(10,56,167))
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
