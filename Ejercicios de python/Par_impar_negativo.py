numero = int(input("Dime tu numero: "))
if( numero<0):
    print("El numero es negativo")
elif (numero % 2 == 0):
    print("El numero es par")
elif (numero % 2 != 0):
    print("El numero es impar")