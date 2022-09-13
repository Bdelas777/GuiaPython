def numero_par_impar(numero):
    if numero > 0: 
        if numero % 2 == 0:
            print("El numero es par")
            return numero
        else:
            print("El numero es impar")
            return numero
    else: 
        return numero
    
numero= int(input("Dame un numero: "))

print("El numero es ",numero_par_impar(numero))