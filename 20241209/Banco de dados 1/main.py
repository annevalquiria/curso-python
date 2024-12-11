#coding: utf-8

import sqlite3 as sq

def CriarBD(): 
	conexao = sq.connect("Funcionarios.db")
	cursor= conexao.cursor()
	return conexao, cursor

def CriarTabela(): 
	tabela = """
	create table if not exists Funcionarios(
		id integer primary key, 
		nome text not null, 
		cargo text not null, 
		dataContratacao text not null); 
		"""
	return tabela

def InserirDados(conexao, cursor, i): 
	nome = input('Digite um nome:')
	cargo = input('Digite um cargo:')
	data = input('Digite uma data no formato aaaa-mm-dd:')
	cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)",(i, nome, cargo, data))
	conexao.commit()
	
if __name__=="__main__": 
	conexao, cursor  = CriarBD()
	tabela = CriarTabela()
	cursor.execute(tabela) 
	conexao.commit()
	for i in range(3): 
		InserirDados(conexao, cursor, i)
	

