'''else significa sino pasa algo has esto y elif sino pasa algo y si '''
print("Verificacion de acceso")
def chequeo_edad():
	edad_usuario=int(input("Introduzca su edad "))
	if edad_usuario<18:
		print("No puedes acceder")
	elif edad_usuario>100:
		print("Edad incorrecta")
	else:
		print("puedes pasar")
	print("Programa finalizado")

nota_usuario=int(input("Introduzca su nota "))
if nota_usuario<5:
	print("Insuficiente")
elif nota_usuario<6:
	print("Suficiente")
elif nota_usuario<7:
	print("Bien")
elif nota_usuario<9:
	print("Notable")
else:
	print("Sobresaliente")

print("Programa finalizado")