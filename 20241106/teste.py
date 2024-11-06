#coding: utf-8

def CriaMatriz(NumLinhas, NumColunas): 
	matrizA = [None]*NumLinhas
	for i in range(NumLinhas): 
		matrizA[i] = [None]*NumColunas
	return matrizA

def ImprimirMatriz(M): 
	NumLinhas = len(M)
	NumColunas = len(M[0])
	for i in range(NumLinhas): 
		for j in range(NumColunas): 
			print(M[i][j], end = " ")
		print()	

def PreencheMatrizPorLinhas(M): 
	NumLinhas = len(M)
	NumColunas = len(M[0])
	print("NumLinhas = ", NumLinhas)
	for i in range(NumLinhas): 
		for j in range(NumColunas): 
			M[i][j]=i*NumColunas+j+1
	ImprimirMatriz(M)
	return M		

def PreencheMatrizPorColunas(M): 
	NumLinhas = len(M)
	NumColunas = len(M[0])
	print("NumLinhas = ", NumLinhas)
	for i in range(NumLinhas): 
		for j in range(NumColunas): 
			M[i][j]=j*NumLinhas+i+1
	ImprimirMatriz(M)
	return M		
	

if __name__ == "__main__": 
	A=CriaMatriz(4,3)			
	PreencheMatrizPorLinhas(A)