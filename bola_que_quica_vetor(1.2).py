import cv2
import numpy as np


#cores
white = (255,255,255)
green = (0,255,0)
red = (0,0,255)

#vetor de força (lista)
velocidade = [2,5]

#posicao inicial da bola (lista)
coordenadas = [300,300]
centro_x = coordenadas[0]
centro_y = coordenadas[1]

#tamanho da bola(raio)
radius = 50
diameter = radius*2

#largura e altura
width = 640
height = 480

color = green
for frame in range(0,600):#600 = 10 segundos de 60 frames
    if (coordenadas[0] + radius > width) or (coordenadas[0] - radius < 0):#se x passa o valor de largura ou x é menor do que 0
                              # (serve para o x ultrapassar a esquerda)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        velocidade[0] = velocidade[0] * -1


    if (coordenadas[1] + radius > height) or (coordenadas[1] - radius < 0):#se y passa o valor de altura
                               #(serve para o y ultrapassar acima)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        velocidade[1] = velocidade[1] * -1

    coordenadas[0] = coordenadas[0] + velocidade[0]#aumentando a velocidade de x
    coordenadas[1] = coordenadas[1] + velocidade[1]#aumentando a velocidade de y


    #tela
    #altura,largura,rgb,tipo de rgb
    canvas = np.zeros((height, width, 3), dtype="uint8")
    #matriz,coordenadas(x,y),tamanho do circulo,cor
    cv2.circle(canvas, (coordenadas[0],coordenadas[1]),radius, color)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(20)