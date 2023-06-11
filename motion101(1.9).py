from bola_oop import Bola
import cv2,math,random
import numpy as np
arrayBola = [] #Lista de todas as bolas em execução

radius = 20

max_bolas = 1000

def cria_bola(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #Construtor            x,y,ang,radius
         arrayBola.append(Bola(x,y,random.randint(0, 360),radius,np.random.randint(0, high=256, size=(3,)).tolist()))#Se eu usar o double click ele insere as bolas no 'arrayBola'


#largura e altura
width = 640
height = 480


canvas = np.zeros((height, width, 3), dtype="uint8")
cv2.namedWindow("Canvas")
cv2.setMouseCallback('Canvas', cria_bola)

frame = 0

while True:
#for frame in range(0,600):#600 = 10 segundos de 60 frames
    for bola_i in arrayBola:# Percorre todas as bolas no frame


        if (bola_i.x + bola_i.radius > width):#se a bola bateu na direita

            #bola_i.color = np.random.randint(0, high=256, size=(3,)).tolist()
            bola_i.velocidade[0] = bola_i.velocidade[0] * -1
            bola_i.ang += 180 #Inverte o angulo quando bate
            if len(arrayBola) < max_bolas:#Se o número de bolas está dentro do limite maximo ele cria a bola
                #Se a bola bateu na direita ele vai criar uma nova bola um pouco para esquerda
                arrayBola.append(Bola(bola_i.x - (bola_i.velocidade[0] + radius), bola_i.y, bola_i.ang,radius,bola_i.color))

        if (bola_i.x - bola_i.radius < 0):#se a bola bateu na esquerda

            #bola_i.color = np.random.randint(0, high=256, size=(3,)).tolist()
            bola_i.velocidade[0] = bola_i.velocidade[0] * -1
            bola_i.ang += 180#Inverte o angulo quando bate
            if len(arrayBola) < max_bolas:
                # Se a bola bateu na esquerda ele vai criar uma nova bola um pouco para direita
                arrayBola.append(Bola(bola_i.x + (bola_i.velocidade[0] + radius), bola_i.y, bola_i.ang,radius,bola_i.color))


        if (bola_i.y + bola_i.radius > height) :#se a bola bateu no chao

            #bola_i.color = np.random.randint(0, high=256, size=(3,)).tolist()
            bola_i.velocidade[1] = bola_i.velocidade[1] * -1
            bola_i.ang += 180#Inverte o angulo quando bate
            if len(arrayBola) < max_bolas:
                # Se a bola bateu no chao ele vai criar uma nova bola um pouco para cima
                arrayBola.append(Bola(bola_i.x, bola_i.y - (bola_i.velocidade[1] + radius),bola_i.ang,radius,bola_i.color))

        if (bola_i.y - bola_i.radius < 0):#se a bola bateu no teto

            #bola_i.color = np.random.randint(0, high=256, size=(3,)).tolist()
            bola_i.velocidade[1] = bola_i.velocidade[1] * -1
            bola_i.ang += 180#Inverte o angulo quando bate
            if len(arrayBola) < max_bolas:
                # Se a bola bateu no teto ele vai criar uma nova bola um pouco para baixo
                arrayBola.append(Bola(bola_i.x, bola_i.y + (bola_i.velocidade[1] + radius), bola_i.ang,radius,bola_i.color))



        bola_i.x = math.ceil(bola_i.x + bola_i.velocidade[0]) #atualizando posição de x
        bola_i.y = math.ceil(bola_i.y + bola_i.velocidade[1]) #atualizando posição de y
        cv2.circle(canvas, (bola_i.x, bola_i.y), bola_i.radius, bola_i.color,-1)



        #Diminui a bola a cada 5 frames
        if frame % 5 == 0:
            bola_i.radius -= 1
        #Se o raio da bola for menor que 0 ela é apagada
        if bola_i.radius <= 0:
            arrayBola.remove(bola_i)
    #Controla os frames para garantir a atualização do tamanho das bolas
    # %resto da divisao
    #0,1,2,3,4
    frame = (frame + 1) % 5
    print(frame)
    #                        640*n bolas/max_bolas
    line_length = math.ceil(width * len(arrayBola)/max_bolas)
    cv2.line(canvas, (0, 0), (line_length, 0), (0,255,0), 5)
    cv2.imshow("Canvas", canvas)
    canvas = np.zeros((height, width, 3), dtype="uint8")
    canvas.fill(255)
    cv2.waitKey(20)

