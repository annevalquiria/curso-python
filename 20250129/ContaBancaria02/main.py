#coding: utf-8
import classContaBancaria as CB
import classContaEspecial as CE

'''
def InserirContaBasica(TitularesContaBasica, nome_titular): 
	Conta = CB.ContaBancaria(nome_titular)
	print(f"{nome_titular}, sua conta é {C1.get_Codigo()}")
	TitularesContaBasica.append(Conta)

TitularesContaBasica = []
nome_titular = "Ana Julia"
InserirContaBasica(TitularesContaBasica, nome_titular)
'''
C2 = CE.ContaEspecial("Ana Julia", 2000)
print("Saldo = ", C2.get_saldo())

#Criação do menu para o usuario
'''
flag = 0
while flag==0:
	print("Entre com a transação a fazer: ") 
	print("\t1- Fazer deposito")
	print("\t2- Fazer saque")
	print("\t3- Consultar saldo")
	print("\t4- Consultar Extrato")  
	opcao = input()
	tabela = ['1','2','3','4']
	if opcao not in tabela: 
		print("Opcao não válida. Recomece") 
	else: 
		flag = 1
		#Fazer deposito
		if (opcao == '1'): 
			valor = float(input("Entre com o valor do deposito: ") )
			if valor>0: 	
				C1.Depositar(valor)
				print("Novo saldo: ", C1.get_saldo())
		#fazer saque
		if (opcao =='2'): 
			valor = float(input("Entre com o valor do saque: ") )
			C1.Retirar(valor)
			print("Saldo atual: ", C1.get_saldo())
'''		
		
'''
valor = input("Entre com a retirada: ")
C1.Retirar(float(valor))
'''
#print(f"O saldo atual da conta é {C1.get_saldo()}")		
						

					

