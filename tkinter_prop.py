from tkinter import *

#Cores

cor_1 = '#242323'

window = Tk()
window.title("Janela do Tkinter")
window.geometry('800x600')
window.config(bg=cor_1)

#window.iconphoto(False, PhotoImage(file=''))

#Não deixa a janela ser alterada de tamanho
window.resizable(width=False,height=False)


window.mainloop()
