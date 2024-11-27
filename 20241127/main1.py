#coding: utf-8
import os, shutil

print(os.getcwd())
print(os.listdir())
try:
    os.mkdir("Teste")
except FileExistsError:
    print("Arquvo ja existia")


Caminho1 = os.getcwd()+os.sep+"/main1.py" #os.set é a barra de3 separacao.
os.chdir("Teste")
Caminho2 = os.getcwd()+"/main1.py"
print("Caminho1", Caminho1)
print("Caminho2", Caminho2)
shutil.copy(Caminho1, Caminho2)
import time 
print("Dormindo")
time.sleep(2)
print("Acordei")
Caminho3 = os.getcwd()
shutil.rmtree(Caminho3)
