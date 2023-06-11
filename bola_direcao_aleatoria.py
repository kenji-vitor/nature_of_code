import cv2,random,math
import numpy as np



#angulo aleatorio

angulo = random.randint(0,350)#Gera um angulo de 0 graus a 350 graus(Que da 360)
print("O angulo da bola é de:",str(angulo)+"º")


#cores
white = (255,255,255)
green = (0,255,0)
red = (0,0,255)

#vetor de força (lista)
velocidade = [5,5]

#tamanho da bola(raio)
radius = 50

#posicao inicial da bola (lista)
#Se a coordenada x ou y for menor que o radius ele fica travado em um canto
coordenadas = [random.randint(0+radius,300),random.randint(0+radius,300)]




#largura e altura
width = 640
height = 480

color = green

#Para gerar o angulo que a bola vai aleatoriamente
velocidade[0] = math.ceil(velocidade [0] * math.sin(angulo))
velocidade[1] = math.ceil(velocidade[1] * math.cos(angulo))

for frame in range(0,600):#600 = 10 segundos de 60 frames

    if (coordenadas[0] + radius > width) or (coordenadas[0] - radius < 0):#se x passa o valor de largura ou x é menor do que 0
                              # (serve para o x ultrapassar a esquerda)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        velocidade[0] = velocidade[0] * -1


    if (coordenadas[1] + radius > height) or (coordenadas[1] - radius < 0):#se y passa o valor de altura
                               #(serve para o y ultrapassar acima)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        velocidade[1] = velocidade[1] * -1



    coordenadas[0] = math.ceil(coordenadas[0] + velocidade[0]) #aumentando a velocidade de x
    coordenadas[1] = math.ceil(coordenadas[1] + velocidade[1]) #aumentando a velocidade de y
    print(coordenadas)

    #tela
    #altura,largura,rgb,tipo de rgb
    canvas = np.zeros((height, width, 3), dtype="uint8")
    #matriz,coordenadas(x,y),tamanho do circulo,cor
    cv2.circle(canvas, (coordenadas[0],coordenadas[1]),radius, color)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(20)