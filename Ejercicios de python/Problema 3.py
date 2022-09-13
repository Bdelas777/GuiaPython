def area_trapecio(base_mayor, base_menor, altura):
    resultado = (base_mayor * base_menor)/2 * altura
    if resultado > 0:
        return print(f'El area del trapecio es  {resultado}')
    else:
        return print("negativo")
    

    
base_mayor = float(input("Dame la base mayor: "))
base_menor = float(input("Dame la base menor: "))
altura = float(input("Dame la altura: "))

area_trapecio(base_mayor, base_menor, altura)
