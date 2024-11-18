#coding utf-8

def Demo_max():
    vet = [-4, 12, 0, 3]
    nome = "xenia"
    dic = {'Igor':18, 'Xenia':13, 'Ana Julia':16, 'Rafael':21}
    print(f"O maior valor do vetor é: {max(vet)}")
    print(f"A letra mais adiantada de {nome} é {max(nome)}")
    print(f"Metrica no dicionario: {max(dic)}")

if __name__=="__main__":
    Demo_max()