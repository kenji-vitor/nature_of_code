import numpy as np
import random,math
class Bola:

    def __init__(self,x,y,ang,radius,color):  # Colocamos atributos para descrever o que o objeto é ou tem
        self.x = x
        self.y = y
        self.ang = ang
        self.radius = radius
        self.velocidade = [5,5]
        self.color = color
        # Para gerar o angulo que a bola vai aleatoriamente
        self.velocidade[0] = math.ceil(self.velocidade[0] * math.sin(ang))
        self.velocidade[1] = math.ceil(self.velocidade[1] * math.cos(ang))

