#coding: utf-8
def TruncadorStringNumerica(Resultado, Ncasas):
	print("L3, ", Resultado)
	Resultado=Resultado.split(".")
	ParteInteira = Resultado[0]	
	ParteFrac = Resultado[1] 
	print("L7", ParteInteira, ParteFrac)
	FlagInt = False
	if ParteFrac=='0': 
		FlagInt = True
	print(FlagInt)
	strg = ''
	if FlagInt:
		strg = ParteInteira
	else: 
		strg = ParteInteira+"."+ParteFrac[0:Ncasas]	
	return(strg)	 

a = 95
b = 35 

div = str(a/b)
Retorno = TruncadorStringNumerica(div,4)
print(Retorno)

	
'''
print(div)
divInt = a//b
print(divInt)
strg1 = int(str(div-divInt).split('.')[1])
print("L10", strg1)
strg1 = f"{divInt}"+'.'#+f"{strg1:.3f}"
print("DivInt: ", strg1)
'''
#parteDec = 89/9-89//9
#strg = str(strg1)+str(parteDec)
'''
sol = eval(strg)
print(sol)
print(type(sol))
resp = ''
print(isinstance(sol, float))
if isinstance(sol, float): 
	resp = f"{sol:.3f}"
print(resp)	
'''
