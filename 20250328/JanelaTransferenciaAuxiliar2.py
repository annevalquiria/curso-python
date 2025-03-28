#coding: utf-8

import tkinter as tk
from classCliente import *
from PIL import ImageTk, Image
from JanelaTransferenciaAuxiliar1 import *
  
#Pagina de Transferencia
class JanelaTransferenciaAuxiliar2():
	def CriarFrameTransferenciaConfirmacaoMovimentacao(self): 
		self.ConfigurarContainerFrameConfirmacaoMovimentacao()	
		self.FrameConfirmacaoMovimentacao()
	
	def ConfigurarContainerFrameConfirmacaoMovimentacao(self): 
		self.ContainerFrameConfirmacaoMovimentacao=tk.Frame(
			self.ContainerTransferenciaContaDestino,
			bg = self.PalhetaCores[8]) #Passa para marrom	
		self.ContainerFrameConfirmacaoMovimentacao.rowconfigure(0, weight = 1) #Cabecalho
		self.ContainerFrameConfirmacaoMovimentacao.rowconfigure(1, weight = 1) #Frame de informacoes	
		self.ContainerFrameConfirmacaoMovimentacao.columnconfigure(0, weight = 2)
		self.ContainerFrameConfirmacaoMovimentacao.grid(row = 1, column = 1,sticky = tk.EW)	
		
	def FrameConfirmacaoMovimentacao(self):
		self.FrameConfirmacaoMovimentacao_Row0()
		self.FrameConfirmacaoMovimentacao_Row1()
		
	def FrameConfirmacaoMovimentacao_Row0(self): 
		Label_ValoresDebitados = tk.Label(
			self.ContainerFrameConfirmacaoMovimentacao,
			fg = "BLACK", 
			height = 3, 
			text = "Resultado da operação:"
			)
		Label_ValoresDebitados.grid(row = 0, column = 0, pady = 5)	
	
			
	def FrameConfirmacaoMovimentacao_Row1(self): 
		Saldo = self.ClienteAtivo.saldo
		Cliente = self.VerificaDestinatario(self.Entry_Titular.get(), self.Entry_CPF.get())
		if (Cliente): #Destinatario existe	
			debito = float(self.Entry_ValorTransferir.get())					
			if (Saldo>=debito): 				
				self.RealizarMovimentacao(
					self.ClienteAtivo.nome, 
					self.Entry_Titular.get(), 
					float(self.Entry_ValorTransferir.get())
					)
				self.ClienteAtivo.saldo-= debito	
				self.AtualizaSaldoBD(self.ClienteAtivo.CPF, debito, self.Entry_CPF.get() )
				self.CriarFrameConfirmacaoMovimentacao()					
			else: 
				print("Saldo insuficiente")
				self.CriarFrameNegacaoMovimentacaoSaldoInsuficiente()					
		else: 
			print("Destinatário do recurso não encontrado.")			
			self.CriarFrameNegacaoMovimentacaoUsuarioNaoEncontrado()
	
	def AtualizaSaldoBD(self, cliente_debitado, debito, cliente_creditado ):#Atualiza saldo dos clientes apos movimentacao.
		self.FramePrincipal.cursor.execute("UPDATE Clientes SET saldo = saldo - ? where CPF = ?",(debito, cliente_debitado))
		self.FramePrincipal.cursor.execute("UPDATE Clientes SET saldo = saldo + ? where CPF = ?",(debito, cliente_creditado))		
		self.FramePrincipal.conexao.commit()				

	def CriarFrameNegacaoMovimentacaoUsuarioNaoEncontrado(self): 
		Label_UsuarioNaoEncontrado = tk.Label(
			self.ContainerFrameConfirmacaoMovimentacao,
			fg = "BLACK", 
			height = 3, 
			text = f"Usuário {self.Entry_Titular.get()} não encontrado."
			)
		Label_UsuarioNaoEncontrado.grid(row = 1, column = 0, pady = 5)	
		Label_SaidaUsuarioNaoEncontrado = tk.Label(
			self.ContainerFrameConfirmacaoMovimentacao,
			fg = "BLACK", 
			height = 3, 
			text = f"Operação não realizada."
			)
		Label_SaidaUsuarioNaoEncontrado.grid(row = 2, column = 0, pady = 5)	

	
	def CriarFrameNegacaoMovimentacaoSaldoInsuficiente(self): 
		Label_SaldoInsuficiente = tk.Label(
			self.ContainerFrameConfirmacaoMovimentacao,
			fg = "BLACK", 
			height = 3, 
			text = f"Saldo na conta insuficiente para realizar a operação. "
			)
		Label_SaldoInsuficiente.grid(row = 1, column = 0, pady = 5)	
		Label_MostraFundos = tk.Label(
			self.ContainerFrameConfirmacaoMovimentacao,
			fg = "BLACK", 
			height = 3, 
			text = f"Valor a debitar: {self.Entry_ValorTransferir.get()}. Saldo atual: {self.VerificaSaldo(self.ClienteAtivo.nome)}"
			)
		Label_MostraFundos.grid(row = 2, column = 0, pady = 5)	


		
	
	
	def CriarFrameConfirmacaoMovimentacao(self): 
		Label_ConfirmacaoMovimentacao = tk.Label(
			self.ContainerFrameConfirmacaoMovimentacao,
			fg = "BLACK", 
			height = 3, 
			text = f"Operação realizada com sucesso. "
			)
		Label_ConfirmacaoMovimentacao.grid(row = 1, column = 0, pady = 5)	
		Label_MostraFundos = tk.Label(
			self.ContainerFrameConfirmacaoMovimentacao,
			fg = "BLACK", 
			height = 3, 
			text = f"Valor a debitar: {self.Entry_ValorTransferir.get()}. Saldo atual: {self.ClienteAtivo.saldo}"
			)
		Label_MostraFundos.grid(row = 2, column = 0, pady = 5)	

		
 
	def RealizarMovimentacao(self, TitularOrigem, TitularDestino, valor):
		#Faz as atualizacoes no banco de dados
		print(f"Transferencia de {valor} da conta de {TitularOrigem} para {TitularDestino}")
		print(f"Atualizacoes no bd") 
		#Atualiza saldo nas duas contas. 
		
	
#	def VerificaSaldo(self, Nome): 
#		return 100
	
	def VerificaDestinatario(self, NomeDestinatario, CPF_Destinatario): 
		#Verifica a existencia do destinatario no banco de dados. 
		#Retorna True se existir	
		print(NomeDestinatario, CPF_Destinatario)
		return True	
		#return False		
	

