# Bucle while es un bucle que se repite n veces hasta que la condicion no sea falsa
'''i=1
while i<=10:
	print("Ejecución" + str(i))
	i=i+1
print("Termino la Ejecución")'''
''' #ejemplo didactico
edad=int(input("Introduce la edad, por favor "))
while edad<5 or edad>100:
	print("Edad incorrecta. Vuelve a intentarlo ")
	edad=int(input("Introduce la edad, por favor  "))
print("Gracias por darnos esa información. Puede ingresar")
print("La edad del aspirante es "+ str(edad) +" años" )'''
import math
print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero: "))
intentos=0
while numero<0:
	print("No se puede hallar la raiz de un numero negativo")
	if intentos==2:
		print("Has consumido todos los intentos, el programa a finalizado")
		break #Nos saca del bucle 
	numero=int(input("Introduce un numero: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)# raiz cuadrada
	print("La raiz cuadrada del " + str(numero) + " es " +  str(solucion))