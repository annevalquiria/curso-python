#coding: utf-8
import tkinter as tk 
import PalhetaCores as PC 

class Controlador(tk.Frame):
    def __init__(self, JanPr):
        tk.Frame.__init__(self, JanPr)
        #Chama uma outra classe para construir a pagina sobre a pagina pai.
        self.PagLogin = PaginaLogin(self)
        self.PagLogin.grid(row = 0, column = 0)

        #Criacao do menu de tela
        self.menu = TrocadorTela(self)
        self.menu.grid(row = 1, column = 0)

class TrocadorTela(tk.Frame):
    def __init__(self, JanPr):
        tk.Frame.__init__(self, JanPr)
        #Cuidado com o comando
        self.PagLogin = tk.Button(self, text = "Login", height = 2, width = 16, bg = PC.RosaClaro, command = self.master.PagLogin.tkraise)
        self.PagLogin.grid(row = 0, column = 0)

class PaginaLogin(tk.Frame):
    def __init__(self, JanPr):
        tk.Frame.__init__(self, JanPr)
        #Colocar um label para iniciar a tela de login
        self.Label1=tk.Label(self, text = "Tela de login", height = 5, width = 40, bg = PC.Rosa)
        self.Label1.grid(row = 0, column = 0)
        #Colocacao de nome de usuario e senha
        self.Label_Nome_Usuario = tk.Label(self, text = "Nome do usuario", height = 3, width = 15)
        self.Label_Nome_Usuario.grid(row = 1, column = 0)
        self.Entry_Nome_Usuario = tk.Entry(self)
        self.Entry_Nome_Usuario.grid(row = 1, column = 1)
        self.Label_Senha_Usuario = tk.Label(self, text = "Senha do usuario", height = 3, width = 15)
        self.Label_Senha_Usuario.grid(row = 2, column = 0)
        self.Entry_Senha_Usuario = tk.Entry(self, show = "*")
        self.Entry_Senha_Usuario.grid(row = 2, column = 1)
        



def main():
    JanelaPrincipal = tk.Tk()
    JanelaPrincipal.title("Banco python")
    #Criacao de janela com 70% do tamanho da tela. 
    TamHorJanela = int(JanelaPrincipal.winfo_screenwidth()*0.7)
    TamVerJanela = int(JanelaPrincipal.winfo_screenheight()*0.7)
    #print(TamHorJanela, TamVerJanela)
    TamTela = str(TamHorJanela)+"x"+str(TamVerJanela)
    JanelaPrincipal.geometry(TamTela)
    Pagina0 = Controlador(JanelaPrincipal)
    Pagina0.pack(fill=tk.BOTH)
    JanelaPrincipal.mainloop()



if __name__=="__main__":
    main()
    