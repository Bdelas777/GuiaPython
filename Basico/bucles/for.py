#bucles son repeticiones de lineas de codigo
#lista
'''for i in [1,2,3]:
	print("Hola")'''
'''for i in ["invierno","primavera","otoño"]:
	print(i)'''
#combinado
'''for i in["Bernardo","Sierra","5"]:
	print("Hola",end=" ")# argumento end nos dice como queremos que termine la sentencia'''
#por caracteres
#email=False #booleano
'''
miEmail=input("Introduce tu email: ")
c=0
for i in miEmail:
	if i=="@" or i==".":
		c=c+1 #contador 
if c==2:
	print("Email correcto")
else:
	print("Email incorrecto")'''
#range: Bucle for normal en c++
'''
for i in range(5):
	print(f"valor de la variable {i}")#notacion de concatenacion de valores texto y variables'''
	#5-9
'''for i in range(5,10):
	print(f"valor de la variable {i}")'''
#normal
'''
for i in range(5,50,3):
	print(f"valor de la variable {i}")'''
#len devuelve la longitud de un string
valido=False
email=input("Introduce tu Email: ")
for i in range(len(email)):
	if email[i]=="@":
		valido=True
if valido==True:
	print("Email correcto")
else:
	print("Email incorrecto")