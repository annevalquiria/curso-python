#coding: utf-8
import classContaBancaria as CB

class ContaEspecial(CB.ContaBancaria): 
	def __init__(self, nome_titular, limite_especial): 
		super().__init__(nome_titular)
		self.limite_especial = limite_especial
	

