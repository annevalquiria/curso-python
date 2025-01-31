#coding: utf-8

import datetime as dt 
def data_hora():
    momento = str(dt.datetime.now())
    Meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Ago", "Set", "Out", "Nov", "Dez"]
    dados_momento = momento.split()
    data = dados_momento[0]
    print(data)
    data = data.split("-")
    ano = data[0]
    mes = data[1]
    dia = data[2]
    horario = dados_momento[1].split(":")
    hora = horario[0]
    minuto = horario[1]
    segundo = horario[2]
    return (ano, mes[mes-1], dia, hora, minuto, segundo)

if __name__ == "__main__":
    print("Dados do momento da requisicao:")
    print(f"\tDia = {dia}, Mes = {mes}, Ano = {ano} ")
    print(f"\tInstante: hora = {hora}, Minuto = {minuto}, Segundo = {segundo} ")

 