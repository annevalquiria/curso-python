#coding: utf-8

'''
t_str= "Eu gosto de Python. "
t2_str = "Vamos estudar python. "
t3_str = "Anexacacao de arquivo"
#abertura e gravacao
ft=open("ArqTexto.dat",'w')
ft.write(t_str)
ft.write('\n')
ft.write(t_str)
ft.write('\n')
ft.close()
'''
#Abertura e leitura
ft2 = open("ArqTexto.dat",'r')
linhas = ft2.readlines()
ft2.close()
#Impressão
for i in range(len(linhas)):
print(linhas[i],end = '')
print()