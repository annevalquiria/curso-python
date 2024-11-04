#coding: utf-8


while True:
    try: 
        n = int(input())
    except EOFError as err:
        break
    aprovacao = (2/3)*n 
    votos = map(int, input().split())
    soma = 0 
    for voto in votos: 
        soma+=voto
    #print(soma)
    if (soma>=aprovacao):
        print("impeachment")
    else: 
        print("acusacao arquivada")