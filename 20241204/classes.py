#coding: utf-8

class computador(object): #Informo ao dev que vou colocar metodos.
    def __init__(self, marca, preco, placaVideo):
        self.marca = marca
        self.preco = preco
        self.placaV= placaVideo
        self.processador = input("Digite o processador: ")
    def set_comp(self):
        self.marca = input("Digite a marca do comp")
        self.preco= input("Digite o preco do comp")
        self.pĺacaV = input("Digite a placa de video do comp: ")
        self.processador = input("Digite o processador: ")
    def get_comp(self):
        print("Marca = ", self.marca)
        print("Proc = ", self.processador)
        print("Preco= ", self.preco)
        print("Placa de video = ", self.placaV)

if __name__=="__main__":
    marca = "Daten"
    placaV = "Nvidea"
    Comp1 = computador(marca, 2000, placaV)
    Comp1.get_comp()