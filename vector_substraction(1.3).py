import cv2,mouse
import numpy as np

#W = U - V

#Cores
green = (0, 255, 0)
blue = (255,0,0)
white= (255,255,255)

#U
u = [5,2]

#V

v = [3,4]

#W

w_x = [u[0]-v[0]]
w_y = [u[1]-v[1]]
w = (w_x,w_y)
print("w=",w)

#Resolução
#width = 300
#height = 300

#Função para construir linha

#def cria_linha():
    #canvas = np.zeros((width,height, 3), dtype="uint8")#800x600
    #Se a resolução for muito alta ele não centraliza
    #matriz,posição inicial(x,y),posição final(x,y),cor
    #cv2.line(canvas, (300,0), (0,300), white)#A linha vai do (300,0) ao (0,300)
    #cv2.line(canvas, (0,0), (300,300), blue)#A linha vai do (0,0) ao (300,300)
    #cv2.imshow("Canvas", canvas)
    #cv2.waitKey(0)


#cria_linha()
