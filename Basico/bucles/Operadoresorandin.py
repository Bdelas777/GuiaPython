#Evaluacion de becas
'''print("Programa de Becas")#ejemplo con el operador and y or
distancia=int(input("Introduce la distancia de tu casa a la escuela en km "))
print(distancia)
hermanos=int(input("Introduce el numero de hermanos en el centro "))
print(hermanos)
salario=int(input("Introduce el salario familiar "))
print(salario)
if distancia>40 and hermanos>2 or salario<=20000:
	print("Se te otorgará una beca")
else:
	print("Lo sentimos no pudimos darte beca")'''
'''operador in nos permite evaluar varias condiciones a la vez bajo ciertos parametros'''
print("Asignaturas optativas 2021")
print("Asignaturas optativas: informatica gráfica - pruebas de software - usabilidad y accesibilidad ")
opcion=input("Pon la opcion escogida: ")
asignatura=opcion.lower()
print(asignatura)
if asignatura in("informatica gráfica","pruebas de software","usabilidad y accesibilidad"):
	print("Asignatura escogida: " + asignatura)
else:
	print("Esa asignatura no existe")
#lower() transforma en minisculas
#upper() todo en mayuscyñas
