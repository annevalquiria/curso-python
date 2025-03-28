#coding: utf-8

import tkinter as tk
from classCliente import *
from PIL import ImageTk, Image
from JanelaTransferenciaAuxiliar2 import *
  
#Pagina de Transferencia
class JanelaTransferenciaAuxiliar1(JanelaTransferenciaAuxiliar2): 
	#Frame 0 - Cabecalho (somente imagem)
	def CriarFrameTransferenciaCabecalho(self): 		
		filename = "Imagens/Banner.png"
		img = Image.open(filename)
		img = ImageTk.PhotoImage(img)	
		LabelBanner =tk.Label(
			self.JanelaBase, 
			image = img, 			
			)
		LabelBanner.image = img
		LabelBanner.grid(row = 0, column = 0, sticky = tk.EW)#, columnspan = 2)		
	
	#Frame 1 - Conta Destino
	def CriarFrameTransferenciaContaDestino(self): 	
		self.ConfigurarContainerFrameTransferenciaContaDestino()
		self.FrameTransferenciaContaDestinoRows()	
	
	def ConfigurarContainerFrameTransferenciaContaDestino(self):	
		self.ContainerTransferenciaContaDestino=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[8]) #Passa para marrom	
		self.ContainerTransferenciaContaDestino.rowconfigure(0, weight = 1) #Cabecalho
		self.ContainerTransferenciaContaDestino.rowconfigure(1, weight = 1) #Dados do destinatario	
		self.ContainerTransferenciaContaDestino.rowconfigure(2, weight = 1) #Valor a transferir e verificacao senha
		self.ContainerTransferenciaContaDestino.rowconfigure(3, weight = 1) #Botao Finalizar
		self.ContainerTransferenciaContaDestino.columnconfigure(0, weight = 2)
		self.ContainerTransferenciaContaDestino.columnconfigure(1, weight = 3)
		#self.ContainerTransferenciaContaDestino.columnconfigure(2, weight = 3)		
		self.ContainerTransferenciaContaDestino.grid(row = 1, column = 0,sticky = tk.EW)	
	
	def FrameTransferenciaContaDestinoRows(self): 
		self.FrameTransferenciaContaDestino_Row0()
		self.FrameTransferenciaContaDestino_Row1()
		self.FrameTransferenciaContaDestino_Row2()
		self.FrameTransferenciaContaDestino_Row3()

	#Frame 2 - Row 0: 
	def FrameTransferenciaContaDestino_Row0(self):		
		Label_ContaCreditar = tk.Label(
			self.ContainerTransferenciaContaDestino,
			fg = "BLACK", 
			height = 3, 
			text = "Conta a creditar:"
			)
		Label_ContaCreditar.grid(row = 0, column = 0, pady = 5)	
	
	#Frame 2 - Row 1:	
	def FrameTransferenciaContaDestino_Row1(self):			
		self.ContainerFrameTransferenciaContaDestino_Row1=tk.Frame(
			self.ContainerTransferenciaContaDestino, 
			bg = self.PalhetaCores[7]) 		
		self.ContainerFrameTransferenciaContaDestino_Row1.rowconfigure(0, weight = 1) 
		self.ContainerFrameTransferenciaContaDestino_Row1.columnconfigure(0, weight = 1)	
		self.ContainerFrameTransferenciaContaDestino_Row1.columnconfigure(1, weight = 1)	
		self.ContainerFrameTransferenciaContaDestino_Row1.grid(row = 1, column = 0,sticky = tk.EW)		
		Titular_Usuario = tk.Frame(
			self.ContainerFrameTransferenciaContaDestino_Row1,
			bg = self.PalhetaCores[2],		
			)
		Titular_Usuario.rowconfigure(0, weight = 1) 
		Titular_Usuario.rowconfigure(1, weight = 1)	
		Titular_Usuario.columnconfigure(0, weight = 1)
		Titular_Usuario.columnconfigure(1, weight = 1)	
		Titular_Usuario.grid(row=0)		
		Nome_Usuario = tk.Label(
			Titular_Usuario,
			fg = "BLACK", 
			height = 4, 
			text = "Titular:"
			)
		Nome_Usuario.grid(row = 0, column = 0, pady = 5)	
		self.Entry_Titular = tk.Entry(Titular_Usuario)		
		self.Entry_Titular.grid(row = 0, column=1)	
		CPF_Usuario = tk.Label(
			Titular_Usuario,
			fg = "BLACK", 
			height = 4, 
			text = "CPF:"
			)
		CPF_Usuario.grid(row = 1, column = 0, pady = 5)		
		self.Entry_CPF = tk.Entry(Titular_Usuario)		
		self.Entry_CPF.grid(row = 1, column=1)

		
	#Frame 2 - Row 2: 
	def FrameTransferenciaContaDestino_Row2(self):					
		self.ContainerFrameTransferenciaContaDestino_Row2=tk.Frame(
			self.ContainerTransferenciaContaDestino, 
			bg = self.PalhetaCores[7]) 		
		self.ContainerFrameTransferenciaContaDestino_Row2.rowconfigure(0, weight = 1) 
		#self.ContainerFrameTransferenciaContaDestino_Row2.rowconfigure(1, weight = 1) 
		#self.ContainerFrameTransferenciaContaDestino_Row2.rowconfigure(2, weight = 1) 
		self.ContainerFrameTransferenciaContaDestino_Row2.columnconfigure(0, weight = 1)		
		#self.ContainerFrameTransferenciaContaDestino_Row2.columnconfigure(1, weight = 1)		
		self.ContainerFrameTransferenciaContaDestino_Row2.grid(row = 2, column = 0,sticky = tk.EW)
		CamposValores = tk.Frame(
			self.ContainerFrameTransferenciaContaDestino_Row1,
			bg = self.PalhetaCores[4],		
			)
		CamposValores.rowconfigure(0, weight = 1) 
		CamposValores.rowconfigure(1, weight = 1)	
		CamposValores.columnconfigure(0, weight = 1)
		CamposValores.columnconfigure(1, weight = 1)	
		CamposValores.grid(row=1)			
		Valor_Transferir = tk.Label(
			CamposValores,
			fg = "BLACK", 
			height =4, 
			text = "Valor a transferir:"
			)
		Valor_Transferir.grid(row = 0, column = 0, pady = 5)	
		self.Entry_ValorTransferir = tk.Entry(CamposValores)		
		self.Entry_ValorTransferir.grid(row = 0, column=1)			
		Conferencia_senha = tk.Label(
			CamposValores,
			fg = "BLACK", 
			height = 4, 
			text = "Digite sua senha: "
			)
		Conferencia_senha.grid(row = 1, column = 0, pady = 5)	
		self.Entry_ConferenciaSenha = tk.Entry(CamposValores, show = "*")		
		self.Entry_ConferenciaSenha.grid(row = 1, column=1)	

	
	def FrameTransferenciaContaDestino_Row3(self):		
		#insercao do botao
		def _command_ButtonRealizarTransferencia(): 
			self.CriarFrameTransferenciaConfirmacaoMovimentacao() #Abre Resultados da movimentacao, JanelaTransferenciaAuxiliar2
		ButtonRealizarTransferencia = tk.Button(
			self.ContainerTransferenciaContaDestino,
			bg = self.PalhetaCores[1], 
			height = 2, 
			text = "Realizar Transferência", 
			command = _command_ButtonRealizarTransferencia
			)		
		ButtonRealizarTransferencia.grid(row = 3, column=0)	
			




		
