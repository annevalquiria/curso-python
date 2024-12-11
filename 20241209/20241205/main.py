
#coding: utf-8

from ClassePasta import *
from ClasseArquivoPastaSuspensa import *

def CriarPasta(QdeArquivos=5): 	
	Pasta1 = Pasta() #Crio a pasta
	Pasta1.CriarPastaVazia()	
	for _ in range(QdeArquivos):		
		Pasta1.Receber_arquivo()
	Pasta1.get_chaves_arquivos_pasta()
	return Pasta1				
		 	
def CriarArquivo(): 
	Arq1 = ArquivoPastaSuspensa("amarelo", "Pesquisa",NumMaxPastas=20)		
	return Arq1

if __name__ == "__main__": 
	Arq = CriarArquivo()	
	'''	
	Pasta1 = CriarPasta()
	Pasta2 = CriarPasta()
	Arq.ReceberPasta(Pasta1)
	Arq.ReceberPasta(Pasta2)
	Arq.get_pastas()
	'''
	
	for i in range(3): 
		PastaSuspensa = CriarPasta()
		Arq.ReceberPasta(PastaSuspensa)
	Arq.get_pastas()		 
	
	
	
	'''
	PastasMat = []
	for i in range(3): 
		Pasta = CriarPasta()
		PastasMat.append(Pasta)
	'''
	
	
	'''
	Pasta1 = Pasta() #Crio a pasta
	Pasta1.CriarPastaVazia()
	Pasta1.get_idPasta()
	for _ in range(3): 
		Pasta1.Receber_arquivo()	
	
	Pasta1.get_chaves_arquivos_pasta()	
	Pasta1.Remover_arquivo()
	print("Verificacao de remocao: ")
	Pasta1.get_chaves_arquivos_pasta()		
	'''

		
