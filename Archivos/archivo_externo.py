'''
Crea la persistencia de datos.Para almacenarlos se puede guardar en archivos externos o BBDD
'''
from io import open
#creacion de archivo externo
'''
archivo_texto=open("archivo.txt","w")#pide 2 argumentos nombre y modo lectura(r)/escritura(w)/append(a)
frase="Estupendo día para estudiar python \n el martes"
archivo_texto.write(frase)#solo nos pide que queremos escribir
archivo_texto.close()#cerrado de archivo'''
'''
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()#read lee decimos que lea 
archivo_texto.close()
print(texto)
'''
'''
archivo_texto=open("archivo.txt","r")
lineas_texto=archivo_texto.readlines()#readlines() lee la informacion line a linea y la almacena en una lista
archivo_texto.close()
print(lineas_texto) # se accede por medio de indice ejemplo [0]
'''
'''
archivo_texto=open("archivo.txt","a")#append
archivo_texto.write("\n siempre es buena idea aprender a programar")
archivo_texto.close()'''
#puntero o cursor

#archivo_texto=open("archivo.txt","r+")#r+ lectura y escritura
#archivo_texto.seek(11)#metodo seek nos posiciona el puntero de acuerdo al caracter
#print(archivo_texto.read(11))#en read se puede limitar la lectura hasta donde quieras segun posicion
#print(archivo_texto.read())
#archivo_texto.seek(len(archivo_texto.read())/2)
#archivo_texto.seek(len(archivo_texto.readline()))
#print(archivo_texto.read())
#archivo_texto.write("Comienza el texto")
#print(archivo_texto.readlines())#readlines es por lista
'''
lista_texto=archivo_texto.readlines()
lista_texto[1]="esta linea a sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)#agregar listas
archivo_texto.close()'''