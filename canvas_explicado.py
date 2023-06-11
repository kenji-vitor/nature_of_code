import cv2
import numpy as np

import time
white = (255,255,255)
        #.zeros para criar o fundo preto     #ALTURA E LARGURA
canvas = np.zeros((300, 300, 3), dtype="uint8") #300x300 e rgb(3 CORES) de cada posição
green = (0, 255, 0)#255 pq é bgr(Não sei pq)
        #matriz(Tela),(posição inicial), (posição final), cor
cv2.line(canvas, (0, 0), (300, 300), green)
red = (0, 0, 255)
                                        #grossura da linha
cv2.line(canvas, (300, 0), (0, 300), red, 10)
# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
# draw another rectangle, this one red with 5 pixel thickness
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
# draw a final rectangle (blue and filled in )
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.rectangle(canvas, (200, 50), (225, 125), white, 1)
#.imshow mostra imagem
# nome da janela,matriz
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# re-initialize our canvas as an empty array, then compute the
# center (x, y)-coordinates of the canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)
# loop over increasing radii, from 25 pixels to 150 pixels in 25
# pixel increments
for r in range(0, 175, 25):
	# draw a white circle with the current radius size
	cv2.circle(canvas, (centerX, centerY), r, white)
# show our work of art
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)




# let's draw 25 random circles
for frames in range (0, 601):
    # re-initialize our canvas once again
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    for i in range(0, 25):
        # randomly generate a radius size between 5 and 200, generate a
        # random color, and then pick a random point on our canvas where
        # the circle will be drawn
                                      #distancia do raio de 5 a 200 aleatorizados
        radius = np.random.randint(5, high=200)
                                               #RGB aleatorizado
        color = np.random.randint(0, high=256, size=(3,)).tolist()
                                                #x e y aleatorizados
        pt = np.random.randint(0, high=300, size=(2,))
        # draw our random circle on the canvas
        cv2.circle(canvas, tuple(pt), radius, color, 0)
    # display our masterpiece to our screen
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(1)