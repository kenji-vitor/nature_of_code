import numpy as np
import cv2 as cv
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:#Se eu apertar o mouse 2 vezes ele cria uma bola
        cv.circle(img,(x,y),10,(255,0,0),-1)
# Create a black image, a window and bind the function to window
img = np.zeros((800,600,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    cv.waitKey(20)
#if cv.waitKey(20) & 0xFF == 27:
        #break
#cv.destroyAllWindows()