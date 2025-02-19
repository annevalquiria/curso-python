#coding: utf-8


import tkinter as tk

'''
Pode ficar passeando entre os botoes. 

'''
from JanelaBase import *
from JanelaApresentacao import *
from JanelaLogin import *
from JanelaUsuario import *

class JanelaRaiz(
		tk.Tk, 
		JanelaBase,
		JanelaApresentacao,
		JanelaLogin,
		JanelaUsuario,
		): 
	def __init__(self): 
		super().__init__()
		self.TituloApp = "Banco Python"
		self.title(self.TituloApp)
		self.set_PalhetaCores()
		self.ConfiguraTelaInicial()
		self.FramePrincipal = self
		self.Paginas = [self.PaginaApresentacao, self.PaginaLogin, self.PaginaUsuario]	#requer as funcoes operando		
		self.CriaJanelaBase()		
		self.Paginas[1]()
		self.mainloop()
			
	def ConfiguraTelaInicial(self): 
		self.TamHorJanela = int(self.winfo_screenwidth()*0.6)
		self.TamVertJanela = int(self.winfo_screenheight()*0.8)	
		self.TamTela = str(self.TamHorJanela)+"x"+str(self.TamVertJanela)		
		self.geometry(self.TamTela)
		self.config(bg = self.PalhetaCores[0])
		
	def set_PalhetaCores(self): 
		self.PalhetaCores = [
			"#222448", #Azul escuro.
			"#54527E", #Roxo claro
			"#c0f0c0", #Verde claro
			"#93bd93", #Verde Ifsc
			"WHITE", 
			"CYAN",
			"GREEN",
			"ORANGE",
			"BROWN",	
			"#f2bfee", #Rosa fofo	
			]
		
if __name__=="__main__": 
	InstanciaRaiz = JanelaRaiz()
	
	

