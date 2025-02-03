#coding: utf-8

import tkinter as tk 

janela = tk.Tk()
strg = "Texto qualquer"
Rotulo = tk.Label(text = strg) #Cria o widget
Rotulo.pack() #Coloca o widget na tela
janela.mainloop()