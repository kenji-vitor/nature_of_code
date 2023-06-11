import mouse

#Mouse


# clique esquerdo
#mouse.click('left')

#clique direito
#mouse.click('right')

# clique do meio
#mouse.click('middle')

#printa a posição atual do mouse
print(mouse.get_position())

#segura algum arquivo/executavel mas não solta
#mouse.hold('left')

# leva o mouse da posição inicial x,y(0,0) para a posição final x,y(1349,695) em 1.5s
#Se absolute=True:

#O mouse vai começar da posição inicial e vai ir até a posição final
#mouse.drag(0, 0, 1349, 695, absolute=True, duration=1)

#Se absolute=False:

#O mouse vai começar da posição onde ele está(fazendo com que o (0,0) não tenha tanta importancia)
# e vai ir até a posição final
#mouse.drag(0, 0, 1349, 695, absolute=False, duration=1)

# move a posição x e y

#Se absolute=False:
#a posição inicial(963,541) vira (1063,641) quando é solicitado mover x=100,y=100, somando os valores
#mouse.move(100, 100, absolute=False, duration=0.2)

#Se absolute=True:
#ele vai para a coordenada x=100,y=100 independente de onde meu mouse está atualmente
#mouse.move(100, 100, absolute=True, duration=0.2)

# make a listener when left button is clicked(Não entendi)
#mouse.on_click(lambda: print("Left Button clicked."))

# make a listener when right button is clicked(Não entendi)
#mouse.on_right_click(lambda: print("Right Button clicked."))

# remove the listeners when you want(Não entendi)
#mouse.unhook_all()

# scroll down
#mouse.wheel(-1)

# scroll up
#mouse.wheel(1)

# roda o programa até eu apertar o botão direito do mouse
#events = mouse.record()

# replay these events(Não entendi)
#mouse.play(events[:-1])