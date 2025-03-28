#coding: utf-8

import tkinter as tk
from classCliente import *
from PIL import ImageTk, Image
from JanelaTransferenciaAuxiliar1 import *
  
#Pagina de Transferencia
class JanelaTransferencia(JanelaTransferenciaAuxiliar1): 
	def PaginaTransferencia(self): 
		self.Apaga_frame(self.FramePrincipal)
		self.CriaJanelaBase() 
		self.title("Transferencia de valores entre contas")
		self.ConfigurarPaginaTransferencia()
		self.CriarPaginaTransferencia()
		
	def ConfigurarPaginaTransferencia(self): 
		self.JanelaBase.columnconfigure(0, weight =1)
		self.JanelaBase.rowconfigure(0, weight = 1)	#Somente cabeçalho
		self.JanelaBase.rowconfigure(1, weight = 25)#Dados conta destino		
		self.JanelaBase.rowconfigure(2, weight = 15)#Atualizacao da condição		
		self.JanelaBase.config(bg = self.PalhetaCores[5])	
	
	def CriarPaginaTransferencia(self): 			
		self.CriarFrameTransferenciaCabecalho()
		self.CriarFrameTransferenciaContaDestino()
				
	

