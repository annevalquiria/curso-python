
#coding: utf-8

from ClassePasta import *
from ClasseArquivoPastaSuspensa import *
import time as t

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

def MostrarPastas(Pastas): 
	for i, j in enumerate(Pastas): 
		print(f"Pasta {i} com conteudo {j.conteudo} ")
		for c,k in j.documento.items(): 	
			print(f"\t chave {c} e valor {k}")
	
	
if __name__ == "__main__": 
	
	ArquivosDePastas = []
	Arquivo1 = CriarArquivo()
	NumPastasCriadas = 2
	for _ in range(NumPastasCriadas): 
		PastaSuspensa = CriarPasta()
		Arquivo1.Pastas.append(PastaSuspensa)
		t.sleep(1.2) #O programa vai parar por 1.2 segundos para mudar o momento unix
		print("Mudanca de pasta")
	print("Mostrando o arquivo de pasta suspensa")	
	MostrarPastas(ArquivosDePastas)
	print()
	Arquivo1.GravarArquivoPastaSuspensa()
