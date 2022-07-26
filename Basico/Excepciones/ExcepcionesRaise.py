#raise sirve para crear excepciones propias y se pueden personalizar
'''def evaluaedad(edad):
	if edad<0:
		raise TypeError("Negativos no se permiten")
	if edad<20:
		return "Eres muy joven"
	if edad<40:
		return "Eres joven"
	if edad<60:
		return "Eres maduro"
	if edad<100:
		return "Cuidate"

print(evaluaedad(15))   '''
import math
def CalculoRaiz(num1):
	if num1<0:
		raise ValueError ("No hay raices negativas ")
	else:
		return math.sqrt(num1)

op1=int(input("Introduce un numero "))
try:
	print(CalculoRaiz(op1))
except ValueError as ErrordeNegativos:
	print(ErrordeNegativos)

print("Programa finalizado")
