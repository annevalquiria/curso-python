#coding: utf-8


import tkinter as tk
#Pagina de usuario
class JanelaUsuario(): 
	def PreencheFrameUsuario(self): 		
		self.JanelaBase.columnconfigure(0, weight =1)#https://www.pythontutorial.net/tkinter/tkinter-grid/
		self.JanelaBase.rowconfigure(0, weight = 4)
		self.JanelaBase.rowconfigure(1, weight = 1)		
		self.JanelaBase.config(bg = self.PalhetaCores[9])
		
	def CriarPaginaUsuario(self): 		
		self.ContainerPaginaUsuario=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[4]) #Passa para marrom
		self.ContainerPaginaUsuario.rowconfigure(0, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaUsuario.rowconfigure(1, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaUsuario.columnconfigure(0, weight = 3)
		self.ContainerPaginaUsuario.columnconfigure(1, weight = 1)
		self.ContainerPaginaUsuario.columnconfigure(2, weight = 3)
		self.ContainerPaginaUsuario.grid(row = 0, column = 0,sticky = tk.EW)
	
	def PaginaUsuario(self):
		self.Apaga_frame(self.FramePrincipal) #Apaga o que tiver na janela.
		self.CriaJanelaBase() 
		self.PreencheFrameUsuario() 		
		self.CriarPaginaUsuario()
		def Gerar_saldo():
			print("Gerar saldo")
		
		Button1 = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Obter saldo", 
			command = Gerar_saldo
			)		
		Button1.grid(row = 0, column=0)	
		ButtonRetornarInicio = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Botao Retornar", 
			command = self.Paginas[0]			
			)		
		ButtonRetornarInicio.grid(row = 0, column=1)	

		ButtonSair = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Sair do Aplicativo", 
			command = self.FramePrincipal.quit #Tem que colocar a saida do banco de dados, tudo. 
			)		
		ButtonSair.grid(row = 0, column=2)			
		
		
		
