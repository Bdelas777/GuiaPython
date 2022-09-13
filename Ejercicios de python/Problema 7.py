def compara_precios(precio, total):
    if (total-precio < 0 ):
        return " y les faltaría " + str(precio-total)
    else:
        return  " y les sobraria " + str(total-precio)
    

def pastel(tipo_pastel, precio,total):
    if (tipo_pastel == "chocolate"):
        print(f"La cantidad de letras del pastel es {len(tipo_pastel)} {compara_precios(precio, total)} pesos ")
    elif (tipo_pastel == "vainilla"):
        print(f"La cantidad de letras del pastel es {len(tipo_pastel)} {compara_precios(precio, total)} pesos ")
    elif (tipo_pastel == "fresa"):
        print(f"La cantidad de letras del pastel es {len(tipo_pastel)} {compara_precios(precio, total)} pesos ")
    else:
        return print("No existe ese tipo de pastel")
        
    
    
tipo_pastel = input("Dime el tipo pastel: ")
tipo_pastel = tipo_pastel.lower()
precio = int(input("Dame el precio: "))
total =130

pastel(tipo_pastel, precio,total)
