# Pide los lados del triangulo
numero1 =int(input("Dime tu numero: "))
numero2 =int(input("Dime tu numero: "))
numero3 =int(input("Dime tu numero: "))
#Checa si es un triangulo o no porque el tercer lado debe ser mayor
if ( numero3 > numero2+numero1):
    print("Si es un triangulo")
else:
    print("No es un triangulo")