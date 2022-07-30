#continue saltar a la siguiente iteración del bucle
#pass devuelve null cuando lo lee
# else sirve como el condicional if

#continue
'''
for letra in "Python":
	if letra=="h":
		continue #ignora el resto del bucle cuando se cumple 
	print("Viendo la letra: " + letra)'''
'''
nombre="Bernardo de la S"
contador=0
for i in nombre:
	if i==" ":
		continue
	contador+=1

print(len(nombre)) #len longitud de caracteres'''
#pass
'''
while True:
	pass#control c rompe el programa'''
	'''
class(mi clase):
	pass
def function():
		pass
'''		


email=input("Introduce tu email por favor: ")

for i in email:
	if i=="@":
		arroba=True
		break
else:
	arroba=False
#el else solo funciona cuando ya se alla acabado el bucle 
print(arroba)

