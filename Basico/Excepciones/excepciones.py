#excepciones son errores en tiempo de ejecución
#captura de excepción es decirle al codigo has esto si no puedes el programa que se ejecute
'''
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:		
    	return num1/num2
    except ZeroDivisionError:
    	print("No se puede dividir un numero entre 0")
    	return "Operación erronea  "

while True:
	try:
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))		
		operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")
		break
	except ValueError:
		print("Los valores introducidos son incorrectos ")


if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecúción del programa ")'''
#excepcion ejemplo 2
def divide():
	#POsicionamiento de varias excepciones
	try:
		op1=float(input("Introduce el primer número: "))
		op2=float(input("Introduce el segundo número: "))
		print("La division es: " + str(op1/op2))
	#por partes
	
	except ValueError:
		print("Los valores introducidos son incorrectos ")
	except ZeroDivisionError:
		print("No se puede dividir un numero entre 0")
	except:#todas
		print("Ha ocurrido un error ")
	finally:#hace que el codigo se ejecute siempre 
		print("Calculo finalizado")
	

divide()