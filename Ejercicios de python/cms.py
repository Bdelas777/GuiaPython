distancia = float(input("Dame una distancia en centimetros: "))
if ( distancia == 0):
    print("La distancia es 0")
elif(distancia < 0 ):
    print("La distancia es negativa")
else:
    print("La distancia es", distancia/1000)