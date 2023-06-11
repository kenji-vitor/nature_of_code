import cv2
import numpy as np


#cores
white = (255,255,255)
green = (0,255,0)
red = (0,0,255)

#vetor de força
x_speed = np.random.randint(3, high=5)
y_speed = np.random.randint(3, high=5)


#posicao bola
x = np.random.randint(0, high=300)#aleatoriza a posição inicial de x
y = np.random.randint(0, high=300)#aleatoriza a posição inicial de y
radius = 60
#largura e altura
width = 640
height = 480

color = green
for frame in range(0,600):#600 = 10 segundos de 60 frames
    if (x > width) or (x < 0):#se x passa o valor de largura ou x é menor do que 0
                              # (serve para o x ultrapassar a esquerda)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        x_speed = x_speed * -1#inverte a direçao

    if (y > height) or (y < 0):#se y passa o valor de altura
                               #(serve para o y ultrapassar acima)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        y_speed = y_speed * -1#inverte a direçao
    # % = divisao
    x = (x + x_speed) % width #Se o x é maior que a largura(640) ele é teletransportado para o outro lado
    y = (y + y_speed) % height#Se o y é maior que a altura(480) ele é teletransportado para o cima
    print(y)
    #tela
    #altura,largura,rgb,tipo de rgb
    canvas = np.zeros((height, width, 3), dtype="uint8")
    cv2.circle(canvas, (x,y),radius, color)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(10)