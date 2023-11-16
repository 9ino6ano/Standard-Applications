import cv2

image=cv2.imread("xman.png")
grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey)
blur=cv2.GaussianBlur(invert,(21,21),0)
invert_blur=cv2.bitwise_not(blur)

sketch=cv2.divide(grey,invert_blur,scale=260)
cv2.imwrite("Xman-Sketch.png",sketch)