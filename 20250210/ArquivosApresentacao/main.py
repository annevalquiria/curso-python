#coding: utf-8

import tkinter as tk
class JanelaPrincipal(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Título")
		label = tk.Label(self, bd = 15,
			text="Texto qualquer",
			relief = 'groove')
		label.pack(fill=tk.X,
			expand=False, padx=10, pady=5)
		Caixa1 = tk.Label(self, text="Caixa 1", 
			bg="green", fg="white")
		Caixa1.pack(ipadx=20, ipady=20, anchor=tk.E,
			expand=True)
		Caixa2 = tk.Label(self, text="Caixa 2",
			bg="red", fg="black")
		Caixa2.pack(ipadx=20, ipady=20, anchor=tk.W,
			expand=True)
			
if __name__ == "__main__":
	janela = JanelaPrincipal()
	janela.mainloop()

