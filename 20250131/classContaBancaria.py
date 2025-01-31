#coding: utf-8
import random as rn
import Data_hora as dh 

class ContaBancaria(object): 
	def __init__(self, nome_titular):
		self.nome_titular = nome_titular
		self.id_conta = self.GeraCodigoConta()
		self.Saldo = 0
		self.Extrato = [] #lista de strings
		print(f"Conta bancaria de {self.nome_titular}")

	def GeraCodigoConta(self): 
		codigoAleatorio = rn.randint(10000,99999)
		#Fazer uma validacao de código gerado a posteriori
		return codigoAleatorio
	
	def get_Codigo(self):
		return self.id_conta
	
	def get_saldo(self): 
		return 	self.Saldo
	
	def get_extrato(self) :
		return self.Extrato
	
	def Depositar(self, valor): 
		if valor>0: 
			self.Saldo+=valor
			datahora = dh.data_hora()
			strg1 = f"Deposito de {valor} no dia {datahora[2]} de {datahora[1]} de {datahora[0]} ás {datahora[3]}h {datahora[4]}m {datahora[5]}s."
			strg2 = f"Saldo final = {self.Saldo}"
			strg = strg1+'\n\t'+strg2 
			self.Extrato.append(strg)
		else: 
			print("Deposito tem que ser positivo.")
	
	def Retirar(self, valor): 
		if self.Saldo>valor>0: 
			self.Saldo-=valor
		else: 
			print(f"Saldo insuficiente para a retirada de {valor}.")
