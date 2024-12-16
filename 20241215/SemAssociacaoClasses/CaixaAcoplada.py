#coding: utf-8
import time

class CaixaAcoplada(object): 
	def __init__(self):
		self.nivel_max_agua = 5.0
		self.nivel_min_agua = 0.2
		self.nivel_agua = 0
		self.VazaoEntrada = 0.5
		self.VazaoSaida = 0.9
		self.Estado = 0 
		self.AcionamentosFeitos = 0
		print("Caixa Acoplada instalada")

	def EnviarCaixaManutencao(self): 
		print("Processo de desinstalação da caixa")
		EsvaziamentoCompleto = 2
		self.EsvaziarCaixaAcoplada(EsvaziamentoCompleto)
		self.Estado = 0
		print("Caixa desinstalada")
	
	def EsvaziarCaixaAcoplada(self,tipo): 
		if (self.Estado ==1)and(self.nivel_agua==self.nivel_max_agua): 	
			print("Caixa em processo de esvaziamento")
			print("\tInicio do esvaziamento")
			Inicio = time.time()			
			if tipo =='1':
				nivel_final_agua = self.nivel_max_agua/2
			else:
				nivel_final_agua = self.nivel_min_agua	
				
			while (self.nivel_agua>=nivel_final_agua):	
				print("\t\t Nivel de agua = ", self.nivel_agua)
				self.nivel_agua-=self.VazaoSaida				
				time.sleep(0.5)
			if 	self.nivel_agua<self.nivel_min_agua: 
				self.nivel_agua=self.nivel_min_agua
			Fim = time.time()	
			
			print("\t Tempo de operacao: {:.3f}".format(Fim-Inicio))	
			return True
		else: 
			print("Caixa precisa ser iniciada")	
			return False
		
		
		
	def AcionarDescarga(self):
		print("Acionar Descarga")
		print("\tO que você fez?")
		print("\t\t 1: xixi")
		print("\t\t 2: cocô")
		tipo = input() 
		self.EsvaziarCaixaAcoplada(tipo)
		self.EncherCaixaAcoplada()	

	def IniciarUtilizacao(self): 
		self.Estado = 1
		self.IniciarSistemaAgua()
	
	def EncherCaixaAcoplada(self): 
		if self.Estado ==1: 	
			print("Caixa em processo de enchimento")
			print("\tInicio do enchimento")
			Inicio = time.time()
			while (self.nivel_agua<=self.nivel_max_agua):	
				self.nivel_agua+=self.VazaoEntrada
				print("\t\t Nivel de agua = ", self.nivel_agua)
				time.sleep(0.5)
			Fim = time.time()	
			if self.nivel_agua>self.nivel_max_agua:
				self.nivel_agua=self.nivel_max_agua		
			
			print("\t Tempo de operacao: {:.3f}".format(Fim-Inicio))	
			return True
		else: 
			print("Caixa precisa ser iniciada")	
			return False
			
		
		
		
		
	def IniciarSistemaAgua(self):
		print("\t Abertura do sistema de água")	
		Inicio = time.time()
		while(self.nivel_agua<self.nivel_min_agua):
			self.nivel_agua+=self.VazaoEntrada
			time.sleep(0.5)
			print("\t Nivel de agua: ", self.nivel_agua)
		Fim = time.time()
		if self.nivel_agua>self.nivel_min_agua: 
			self.nivel_agua=self.nivel_min_agua
		print("\tTempo de operacao: {0:.1f}".format(Fim-Inicio))	
		
	def get_nivel_agua(self) :
		return 	self.nivel_agua
	
	
	
	
	
