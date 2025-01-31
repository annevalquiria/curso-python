#coding: utf-8

import classContaEspecial as CE 
import classContaBancaria as CB

ContasBasicas = []
Contasespeciais = []
Cb1 = CB.ContaBancaria("Ana Julia")
print("Saldo = ", Cb1.get_saldo())
Cb1.Depositar(500)
t.sleep(2)
Cb1.Retirar(300)
Extrato = Cb1.get_extrato()
for i in range(len(Extrato)):
    print(Extrato[i])
#Ce1 = CE.ContaEspecial("Luciano")