#coding: utf-8

from datetime import datetime
import tkinter as tk
from classCliente import *
from PIL import ImageTk, Image	
from tkinter import messagebox 
  
#Pagina de login
class JanelaSaldoExtrato(): 
	def PaginaAbrirConta(self): 
		self.Apaga_frame(self.FramePrincipal)
		self.CriaJanelaBase() 
		self.title("Transferencia de valores entre contas")
		

