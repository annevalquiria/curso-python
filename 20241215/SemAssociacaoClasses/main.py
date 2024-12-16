#coding: utf-8
import CaixaAcoplada as CA

if __name__=="__main__":
	Vaso = CA.CaixaAcoplada()
	Vaso.IniciarUtilizacao()
	print("Nivel atual de água: ",Vaso.get_nivel_agua())
	Vaso.EncherCaixaAcoplada()
	print("Nivel atual de água: ",Vaso.get_nivel_agua())	
	Vaso.AcionarDescarga()
	print("Nivel atual de água: ",Vaso.get_nivel_agua())
	Vaso.EnviarCaixaManutencao()
