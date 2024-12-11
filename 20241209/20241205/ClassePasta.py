#coding: utf-8
import time as t	#Obtem momento unix em float
import datetime as dt	#Obtem momento unix com data 
import random

class Pasta(object): 
	def __init__(self): 
		self.id = ''
		self.conteudo = ''
		self.estado = 0 	#0 significa pasta vazia, 1 com documento
		self.documento = {}

	def CriarPastaVazia (self): 
		self.id = input("Identificacao da pasta: ")
		self.id = str(int(t.time())) #Nos dá o momento unix. Comentar depois 	
		self.conteudo = input("Entre com o conteudo da pasta: ")
		self.estado = 0
	
	def Receber_arquivo(self):
		#nome =input("Entre com o nome do arquivo: ")  
		#end = input("Entre com o endereco do arquivo: ")
		NomesArquivos = ["Raja", "Francisco", "Luciano", "Ricardo", "Rotundo"] 
		nome = NomesArquivos[random.randint(0,len(NomesArquivos)-1)]
		end = dt.datetime.now()
		#Arquivo será referenciado por um dicionario.		
		if self.documento.get(nome)==None: 
			self.documento[nome] = end
			self.estado = 1
		else: 
			print("Documento contido na pasta. ") 	
	
	def Remover_arquivo(self):
		Arq = input("Entre com a nome do arquivo a remover: ")
		DocumentoRemovido = None
		if self.documento.get(Arq)!=None:
			DocumentoRemovido = self.documento.pop(Arq)
		else: 
			print(f"Documento {Arq} nao encontrado.") 
		return DocumentoRemovido	 	
		
	
	def get_idPasta(self): 
		print("id = ", self.id)
		print("conteudo = ", self.conteudo)
	
	def get_chaves_arquivos_pasta(self): 
		if self.estado ==1: 
			print("Relação dos arquivos na pasta: ", self.id)
			for chave, valor in self.documento.items(): 
				print('\t chave = ',chave, " valor = ", valor)
		else: 
			print("Pasta está vazia") 		
				
