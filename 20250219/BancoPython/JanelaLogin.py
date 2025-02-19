#coding: utf-8


import tkinter as tk
#Pagina de login
class JanelaLogin(): 
	def PreencheFrameLogin(self): 		
		self.JanelaBase.columnconfigure(0, weight =1)#https://www.pythontutorial.net/tkinter/tkinter-grid/
		self.JanelaBase.rowconfigure(0, weight = 4)
		self.JanelaBase.rowconfigure(1, weight = 1)		
		self.JanelaBase.config(bg = self.PalhetaCores[5])
		
	def CriarPaginaLogin(self): 		
		self.ContainerPaginaLogin=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[6]) #Passa para verde forte
		self.ContainerPaginaLogin.rowconfigure(0, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaLogin.rowconfigure(1, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaLogin.columnconfigure(0, weight = 3)
		self.ContainerPaginaLogin.columnconfigure(1, weight = 1)
		self.ContainerPaginaLogin.columnconfigure(2, weight = 3)
		self.ContainerPaginaLogin.grid(row = 0, column = 0,sticky = tk.EW)

	
	def PaginaLogin(self): 
		self.Apaga_frame(self.FramePrincipal) #Apaga o que tiver na janela.
		self.CriaJanelaBase() 
		self.PreencheFrameLogin() 		
		self.CriarPaginaLogin()
		def MudarPagUsuario():
			self.Paginas[2]()
		
		Button1 = tk.Button(
			self.ContainerPaginaLogin, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Botao login", 
			state = tk.ACTIVE, 
			command = MudarPagUsuario
			)		
		Button1.grid(row = 1, column=0)
		'''
		Button2 = tk.Button(
			self.ContainerPaginaApresentacao, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Abra conta para sua empresa"
			)
		Button2.grid(row = 1, column=1)
		ButtonAcessar = tk.Button(
			self.ContainerPaginaApresentacao, 
			bg = self.PalhetaCores[3], 
			#width = 7,
			height = 2, 
			text = "Acessar conta", 
			state = tk.ACTIVE
			)
		ButtonAcessar.grid(row = 1, column=2)
		LabelAcessar = tk.Label(
			self.ContainerPaginaApresentacao, 
			bg = self.PalhetaCores[6], 
			height = 2, 
			text = "Já é cliente? ",	#Colocar moldura				
			)
		LabelAcessar.grid(row = 0, column=2, ipady = 7)
		LabelEspaco = tk.Label(
			self.ContainerPaginaApresentacao, 
			bg = self.PalhetaCores[6], 
			height = 0, 
			)
		LabelEspaco.grid(row = 2, column=2)
		'''

