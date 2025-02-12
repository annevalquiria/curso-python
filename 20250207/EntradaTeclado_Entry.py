#coding:utf-8

import tkinter as tk

def _command_Botao_Raizes():
	a = float(entry_a.get())
	#Resultado_label.config("Raiz legal")
	print(a)

janela = tk.Tk()
janela.title("Calc Eq 2 grau")
janela.geometry("400x400")

#Criacao dos widgets label e widget
#Criacao do widget Label
label_a= tk.Label(janela, text="Coeficiente a:")
label_a.grid(row = 0, column = 0)
#Criacao do widget Entry
entry_a = tk.Entry(janela).grid(row=0, column=1)

#Criacao do widget Label
label_b= tk.Label(janela, text="Coeficiente b:")
label_b.grid(row = 1, column = 0)
#Criacao do widget Entry
entry_b = tk.Entry(janela).grid(row=1, column=1)

#Criacao do widget Label
label_c= tk.Label(janela, text="Coeficiente c:")
label_c.grid(row = 2, column = 0)
#Criacao do widget Entry
entry_c = tk.Entry(janela).grid(row=2, column=1)


#Label para exibir resultado
Resultado_label = tk.Label(janela, text = '')
Resultado_label.grid(row = 4, column = 0)

#Botao para calcular as raizes. 
Button_Calculo = tk.Button(janela, text = "Calcular Raízes", command =_command_Botao_Raizes)
Button_Calculo.grid(row = 3, column = 0, columnspan=2)

janela.mainloop()









