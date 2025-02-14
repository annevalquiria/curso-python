#coding: utf-8 

import tkinter as tk
import sqlite3 as sq #Importacao do banco de dados. 

def CriacaoBancoDados(): 
	NomeBD = "Usuario_senha.db"
	tabelaBD = '''
		CREATE TABLE IF NOT EXISTS Usuario_senha(
			nome TEXT NOT NULL,
			senha TEXT NOT NULL);
			'''
	conexao = sq.connect(NomeBD)
	cursor = conexao.cursor()
	cursor.execute(tabelaBD)
	conexao.commit()
	nome = input("Digite seu nome: ")
	senha = input("Digite sua senha: ")
	conexao.execute("INSERT INTO Usuario_senha VALUES (?,?)", (nome, senha))
	conexao.commit()

class Controlador(tk.Frame):
	def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
		#Chama uma outra classe para construir a pagina sobre a pagina pai.
        #self.BotoesPrincipais()#Funcao para criar botoes 
		self.PagLogin = PaginaLogin(self)
		self.PagLogin.grid(row=0, column = 0)

		#Criacao do menu de tela. 
		self.menu = TrocadorTela(self)
		self.menu.grid(row = 1, column = 0)

   

class PaginaLogin(tk.Frame):
    def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
        self.Label_login1 = tk.Label(self, text = "Pagina de login", height = 5, width = 40, bg = "Dark pink")
        self.Label_login1.grid()


class TrocadorTela(tk.Frame): 
	def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
        self.BotoesPrincipais
		#Cuidado com o comando
		#self.PagLogin = tk.Button(self, text = "Login", height = 2, width = 16, command = self.master.PagLogin.tkraise)			
		#self.PagLogin.grid(row = 0, column = 0)
        self.LabelCentral=tk.Label(self, text = "Banco python", height = 5, width = 52, background = "Pink")
        self.LabelCentral.grid(row = 0, column = 2, columnspan = 1)

    def BotoesPrincipais(self):
        self.BotaoLogin=tk.Button(self, text = "Tela de login", height = 2, width = 16, bg = "Light pink", command = self.master.PagLogin.tkraise)
        self.BotaoLogin.grid(row = 1, column = 2, columnspan = 1)

		

    def main(): 	
	JanelaPrincipal = tk.Tk()
	JanelaPrincipal.title("Banco Python")
	#Criacao de janela com 70% do tamanho da tela. 
	TamHorJanela = int(JanelaPrincipal.winfo_screenwidth()*0.7)
	TamVertJanela = int(JanelaPrincipal.winfo_screenheight()*0.7)
    TamTela = str(TamHorJanela)+"x"+str(TamVertJanela)
	JanelaPrincipal.geometry(TamTela)
	Pagina0 = Controlador(JanelaPrincipal)
	Pagina0.pack(expand = True, fill=tk.BOTH)
	JanelaPrincipal.mainloop()



    if __name__=="__main__": 
	#CriacaoBancoDados()
	main()