#las cadenas son objetos strings y aqui se pondran algunos de los metodos improtantes
'''
upper() Hace mayusculas todas las letras,lower() Hace minusculas todas las letras, capitalize( ) solo pone la 
primera en mayuscula,count() cuenta cuantas veces a aparece una letra o caracter en un grupo de letras o lista,
find() representa la posicion donde aparece caracter o no, isdigit() nos dice si son digitos, isalum() nos dice
si son alfanumericos, isalpha() nos dice si son de letras, split() se para por palabras usando espacios,strip()
borra los espacios principio y final, replace()cambia palabras y rfind() representa el indice de un caracter 
alrevez
'''
edad=input("Introduza su edad: ")
while(edad.isdigit()==False):
	print("Por favor introduce un valor numerico")
	edad=input("Introduza su edad: ")


if int(edad)<18:
	print("No puede pasar")
else:
	print("Puede pasar")
