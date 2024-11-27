#coding: utf-8
import os, shutil

def VerificacaoArquivos():
    Caminho_pasta = os.getcwd()
    Arquivos_pasta = os.listdir()
    '''
    print(Caminho_pasta)
    print(Arquivos_pasta)
    '''
    #Abertura dos arquivos na pasta Textos:
    Pasta_atual = os.chdir("Textos")
    #print(os.getcwd())
    Arquivos_pasta_Textos = os.listdir()
    '''
    print("Arquivos na pasta Textos: ")
    for i, nome in enumerate(Arquivos_pasta):
        print(i, nome)
    '''
    del Arquivos_pasta_Textos[1]
    '''
    print("Arquivos na pasta Texto so com livros: ")
    for i, nome in enumerate(Arquivos_pasta):
        print(i, nome)
    '''
    return Arquivos_pasta_Textos

def Abertura_arquivos(ListaArquivos):
    Caminho_Pasta_Atual = os.getcwd()
    print(os.getcwd)






if __name__=="__main__":
   ListaArquivos = VerificacaoArquivos()