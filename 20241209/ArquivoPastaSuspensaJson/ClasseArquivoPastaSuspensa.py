#coding: utf-8
import json
class ArquivoPastaSuspensa(object):
	def __init__(self, cor, departamento, NumMaxPastas=10): 
		self.cor = cor
		self.depto = departamento
		self.NumMaxPastas = NumMaxPastas
		self.estado = 0
		self.Pastas = [] 
		#print("cor = ", self.cor, "NumPastas = ", self.NumMaxPastas)
	
	def ReceberPasta(self, pasta):
		self.Pastas.append(pasta) 
		self.estado = 1
	
	def get_pastas(self): 
		for i in range(len(self.Pastas)): 
			print("Identificador da pasta: ",self.Pastas[i].id)
			print("Quantidade de documentos: ", len(self.Pastas[i].documento)) 
				 
	def GravarArquivoPastaSuspensa(self): 	
		#Converter todos os documentos para um vetor e transferir para o arquivo. 
		VetorTemporario = [self.Pastas[i].documento for i in range(len(self.Pastas))]
		print(VetorTemporario)
		with open("GravacaoPasta.json", "w", encoding = "utf-8") as gr: 
			json.dump(VetorTemporario,gr)
			
			
