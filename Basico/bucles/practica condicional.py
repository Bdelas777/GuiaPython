#No existen los switch case
'''edad=7
if 0<edad<100:# se puede hacer este tipo de condiciones en python
	print("Edad correcta")
else:
	print("Edad incorrecta")'''
salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salario del presidente: " +str(salario_presidente)) #forma de concatenar
 
salario_director=int(input("Introduce el salario del director: "))
print("Salario del director: " +str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe_area: "))
print("Salario del jefe_area: " +str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("Salario del administrativo: " +str(salario_administrativo))
if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo anda mal")