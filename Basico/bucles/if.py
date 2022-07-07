'''condicional if'''
print("Programa de evalaucion de nota de alumnos ")
nota=input()
def evalaucion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="reprobado"
	return valoracion

print(evalaucion(int(nota)))
