#diccionarios
'''estructuras de datos que se guardan por medio de asociación clave:valor y no tienen orden'''
#midiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
#print(midiccionario["Francia"])#se accede por medio de la clave a lo que esta a dentro
'''midiccionario["Italia"]="Lisboa"#agrega datos al diccionario
print(midiccionario)#impresion completa
midiccionario["Italia"]="Roma"#modificacion del diccionario
print(midiccionario)
del midiccionario["Reino Unido"]#Eliminacion de un elemento del diccionario
print(midiccionario)'''
#midiccionario={"Alemania":"Berlín",23:"Jordan","Mosqueteros":3}#diccioanrio combinado
#print(midiccionario)
'''mitupla=("España","Francia","Reino Unido", "Alemania") #tupla para asignar valores clave
midiccionario={mitupla[0]:"Madrid",mitupla[1]:"París",mitupla[2]:"Londres",mitupla[3]:"Berlín"}
print(midiccionario)'''
midiccionario={23:"Jordan","Nombre": "Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1994,1997,1998]}}
#mas valores en el diccionario y doble diccionario
print(midiccionario.keys())# nos da las claves
print(midiccionario.values())#nos da los valores
print(len(midiccionario))#longitud del diccionario
print(midiccionario)

