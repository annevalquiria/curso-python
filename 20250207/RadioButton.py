#coding: utf-8

import tkinter as tk

def _command_SetButton(): 
	print("valor = ", varInteiraTk.get())
	

janela = tk.Tk()
varInteiraTk = tk.IntVar()
RB1=tk.Radiobutton(janela, text = "Modo 1", variable = varInteiraTk, value=1, command = _command_SetButton)
RB1.pack()

janela.mainloop()


