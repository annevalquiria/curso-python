#coding: utf-8

'''
Controlador de entrada de agua
'''

class ValvulaEntradaAgua(object):
	def __init__(self): 
		self.EstadoValvulaEntrada = "Fechado"
		self.EstadoRefilPerfume = "Cheio"
		print("\tValvula de entrada instalada")
	
	def Abrir_ValvulaEntrada(self): 
		self.EstadoValvulaEntrada ="Aberto"

	def Fechar_ValvulaEntrada(self): 
		self.EstadoValvulaEntrada ="Fechado"
		
	def get_estado_valvula_entrada(self):
		return 	self.EstadoValvulaEntrada

	def set_troca_refil_perfume(self, EstadoRefil):
		if(EstadoRefil==True):
					self.EstadoRefilPerfume = "Vazio"

	def get_estado_refil_perfume(self):
		return self.EstadoRefilPerfume	
