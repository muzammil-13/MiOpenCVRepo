import cv2

image=cv2.imread('lena.png',1)

# Circle [left top] drawing
cv2.circle(image,(50,50),50,(0,0,255),-1)
# Circle2 [left bottom] drawing
cv2.circle(image,(50,462),50,(0,0,255),-1)
# Circle3 [right top] drawing
cv2.circle(image,(462,50),50,(0,0,255),-1)
# Circle4 [right bottom] drawing
cv2.circle(image,(462,462),50,(0,0,255),-1)

# Rectangle drawing
cv2.rectangle(image,(100,200),(400,300),(0,255,0),3)

# Text adding
font=cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(image,'Hi Lena',(150,250),font,1.5,(000,000,100))

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()