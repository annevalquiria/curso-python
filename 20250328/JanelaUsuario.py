#coding: utf-8

from  classCliente import *
import tkinter as tk
from PIL import ImageTk, Image


#Pagina de usuario

class JanelaUsuario(): 
	def PaginaUsuario(self):
		self.Apaga_frame(self.FramePrincipal) #Apaga o que tiver na janela.
		self.CriaJanelaBase()
		self.ClienteAtivo = Cliente()
		self.PesquisaBD() 
		self.ConfigurarPagUsuario() 		
		self.CriarPaginaUsuario()
		self.InsereBannerUsuario()
		self.InsereAnuncio()
		self.ControleBotoes()
		self.title(f"Bem vindo {self.ClienteAtivo.nome}")
		
	def PesquisaBD(self): 
		ConsultaClienteAtivo = "SELECT * FROM Clientes where ativo = 1"			
		self.FramePrincipal.cursor.execute(ConsultaClienteAtivo)	#Posiciona o cursor
		DadosRecebidos = self.FramePrincipal.cursor.fetchall()
		if len(DadosRecebidos)==0: 
			print(DadosRecebidos)
		else: 	
			self.ClienteAtivo.CPF = DadosRecebidos[0][0]
			self.ClienteAtivo.nome = DadosRecebidos[0][1]
			self.ClienteAtivo.senha = DadosRecebidos[0][2]
			self.ClienteAtivo.dataAbertura = DadosRecebidos[0][3]
			self.ClienteAtivo.saldo = DadosRecebidos[0][4]
			self.ClienteAtivo.extrato = DadosRecebidos[0][5]
			self.ClienteAtivo.movimentacoes = DadosRecebidos[0][6]
			self.ClienteAtivo.ativo = DadosRecebidos[0][7]

	def ConfigurarPagUsuario(self): 		
		self.JanelaBase.columnconfigure(0, weight =1)#https://www.pythontutorial.net/tkinter/tkinter-grid/
		self.JanelaBase.rowconfigure(0, weight = 1)
		self.JanelaBase.rowconfigure(1, weight = 15)	
		self.JanelaBase.rowconfigure(2, weight = 20)		
		self.JanelaBase.config(bg = self.PalhetaCores[5])		
				
	def CriarPaginaUsuario(self): 		
		self.ContainerPaginaUsuario=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[8]) #Passa para marrom
		self.ContainerPaginaUsuario.rowconfigure(0, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaUsuario.rowconfigure(1, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaUsuario.columnconfigure(0, weight = 3)
		self.ContainerPaginaUsuario.columnconfigure(1, weight = 1)
		self.ContainerPaginaUsuario.columnconfigure(2, weight = 1)
		self.ContainerPaginaUsuario.columnconfigure(3, weight = 3)
		self.ContainerPaginaUsuario.grid(row = 1, column = 0,sticky = tk.EW)	
	
	def InsereBannerUsuario(self): 
		filename = "Imagens/Banner.png"
		img = Image.open(filename)
		#img =img.resize(int(self.TamHorJanela), int(self.TamVertJanela*0.5))
		#img = img.resize((int(self.TamHorJanela*0.8), int(self.TamVertJanela*0.5)))
		img = ImageTk.PhotoImage(img)	
		LabelBanner =tk.Label(
			self.JanelaBase, image = img
			)
		LabelBanner.image = img
		LabelBanner.grid(row = 0, column = 0, sticky = tk.EW)#, columnspan = 2)	
		
	def InsereAnuncio(self): 
		filename = "Imagens/Teletubbies.jpg"
		img = Image.open(filename)
		#img =img.resize(int(self.TamHorJanela), int(self.TamVertJanela*0.5))
		#img = img.resize((int(self.TamHorJanela*0.8), int(self.TamVertJanela*0.5)))
		img = ImageTk.PhotoImage(img)	
		LabelBanner =tk.Label(
			self.JanelaBase, image = img
			)
		LabelBanner.image = img
		LabelBanner.grid(row = 2, column = 0, sticky = tk.EW, columnspan = 2)		

	def ControleBotoes(self):
		#Funcoes command de botoes:	
		def SaidaApp(): 
			self.FramePrincipal.cursor.execute("UPDATE Clientes SET ativo = ? where CPF = ?",(0, self.ClienteAtivo.CPF))
			self.FramePrincipal.conexao.commit()
			print("Saida do programa") 			
			self.FramePrincipal.quit()						
		#Inicio do curso da função			
		Button1 = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Transferencia entre contas", 
			command = self.Paginas[4]
			)		
		Button1.grid(row = 0, column=1)	
		ButtonRetornarInicio = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Botao Retornar", 
			command = self.Paginas[0]			
			)		
		ButtonRetornarInicio.grid(row = 0, column=2)
		ButtonSair = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Sair do Aplicativo", 
			command = SaidaApp #Tem que colocar a saida do banco de dados, tudo. Utilizar update para ativo passar para zero. 
			)		
		ButtonSair.grid(row = 0, column=3)					
		

