#coding utf-8
'''
Abertura de arquivo por redirecionamento 
Contar palavras
Guardar em arquivo.
'''
Dicionario = {}
TamanhoMinimoPalavra = 4
CaracteresBasicos = '",.!?: -;()'
CaracteresExtras = "'"
CaracteresRemover = CaracteresExtras+CaracteresBasicos
NomeProprio = ['harry', 'hermione', 'hagrid', 'dumbledore', 'snape', 'draco', 'ronnie']
while True:
    try:
        Linha = input().split()
        if Linha != "":
            for i in range(len(Linha)):
                Palavra = (Linha[i].strip(CaracteresRemover)).lower()
                if Palavra not in NomeProprio:
                if (len(Palavra))>=TamanhoMinimoPalavra:
                    k = Dicionario.get(Palavra)
                    if k == None:
                        Dicionario[Palavra]=1
                    else:
                        Dicionario[Palavra]+=1
    except EOFError as Er:
        break
for chave, valor in Dicionario.items():
    print(chave, valor)
