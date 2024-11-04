#coding: utf-8
'''
notas = [100, 50, 20 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
Valor_Entrada = float(input())
print(Valor_Entrada)
Parte_Inteira_Valor_Entrada = int (Valor_Entrada)
Parte_Decimal_Valor_Entrada = Valor_Entrada-Parte_Inteira_Valor_Entrada
print(Parte_Inteira_Valor_Entrada)
print(Parte_Decimal_Valor_Entrada)
print("Problema: A parte decimal fica com residuo de memoria na conversao de base")
print("2 para base 10")
'''


notas = [100, 50, 20 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
QdeNotas = [0]*len(notas) #Faz vetor com quant de notas
QdeMoedas = [0]*len(moedas) #Faz vetor com quant de moedas
Valor_Entrada = input().split('.')
#print(Valor_Entrada)
ParteInteira = int(Valor_Entrada[0])
ParteDecimal = int(Valor_Entrada[1])
#Separacao das notas
ValorInt = ParteInteira 
for i in range(len(notas)):
    while(ValorInt>=notas[i]):
        QdeNotas[i]+=1
        ValorInt-=notas[i]
#print("NOTAS:")
#for i in range(len(notas)):
    #strg = f"{QdeNotas[i]} de R${notas[i]}"
    #print(strg)
#Separacao das moedas
Original_Moedas = moedas.copy()#faco uma copia dos valores originais
#Passando as moedas para valores inteiros
for i in range(len(moedas)):
    moedas[i]*=100
    moedas[i]= int(moedas[i])
#print("Parte decimal", ParteDecimal)
#print(moedas)
ValorInteiro = ParteDecimal+ValorInt*100 #Pode ter sobra de 1 real nas notas
for i in range(len(moedas)):
    while(ValorInteiro>=moedas[i]): #O vetor moedas foi multiplicado por 100
        QdeMoedas[i]+=1
        ValorInteiro-=moedas[i]
print("MOEDAS:")
for i in range(len(notas)):
    strg