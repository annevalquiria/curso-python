#coding: utf-8
import random as rn

class ContaBancaria(object): 
	def __init__(self, nome_titular):
		self.nome_titular = nome_titular
		self.id_conta = self.GeraCodigoConta()
		self.Saldo = 0
		self.Extrato = [] #lista de strings
	
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
		else: 
			print("Deposito tem que ser positivo.")
	
	def Retirar(self, valor): 
		if self.Saldo>valor>0: 
			self.Saldo-=valor
		else: 
			print(f"Saldo insuficiente para a retirada de {valor}.")
