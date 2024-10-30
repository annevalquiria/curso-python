#coding: utf-8

def aprovar_pessoa(nome):
    return nome+" APROVADO"
nomes = ['Larissa', 'Rafael', 'Marcos', 'Joao']
print(nomes)

'''
for i in range (len(nomes)):
    nomes[i] = aprovar_pessoa(nomes[i])
print(nomes)
'''
situacao = list(map(aprovar_pessoa, nomes))
nomes = list(map(aprovar_pessoa, nomes))
print(situacao)
print(nomes)

def map2():
    print('Entre com uma quantidade de numeros: ')
    A  = input().split()
    B = list(map(float, A))
    print(A)
    #print(B)


    if __name__=="__main__": 
        map2()
        #map1()