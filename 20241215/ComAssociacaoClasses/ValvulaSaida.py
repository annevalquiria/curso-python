#coding: utf-8

'''
Controlador de saida de agua
'''

class ValvulaSaidaAgua(object):
	def __init__(self): 
		self.EstadoValvulaSaida1 = "Fechado" #xixi
		self.EstadoValvulaSaida2 = "Fechado" #cocô
		print("\tValvula de Saida instalada")
	def Abrir_ValvulaSaida(self, tipo): 
		if(tipo =='1'):
			self.EstadoValvulaSaida1 = "Aberto"
		else: 	
			self.EstadoValvulaSaida2 ="Aberto"

	def Fechar_ValvulaEntrada(self): 
		self.EstadoValvulaSaida1 ="Fechado"
		self.EstadoValvulaSaida2 ="Fechado"
		
	def get_estado_valvula_entrada(self):
		return 	self.EstadoValvulaSaida1, self.EstadoValvulaSaida2
			

