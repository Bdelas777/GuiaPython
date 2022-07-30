#tuplas: listas que no se pueden modificar
#no se puede añadir,eliminar o mover elementos(append,remove o extend) y permiten un index se usa igual como lista
#parentesis opcionales
#mitupla=("Bernardo",5,7,2002)
#print(mitupla[2])#acceso a la tupla
#metodos de converción de tupla  a lista
#milista=list(mitupla)
#print(milista)
#proceso inverso
#milista=["Bernardo",5,7,2002]
#mitupla=tuple(milista)
#print(mitupla)
#print("Bernardo" in mitupla)#in nos devuelve true si encuentra elemento y false sino
#print(mitupla.count("Bernardo") ) #count nos dice cuantas veces se encuentra un elemento en la tupla
#print(len(mitupla))#len averigua la longitud de la tupla
#tupla unitaria
#mitupla=("Alfonso",)
#print(len(mitupla))
#tupla sin parentesis se llama empaquetado de tupla
#mitupla="Bernardo",5,7,2002
#print(mitupla)
#desempaquetado de una tupla
mitupla=("Bernardo",5,7,2002)
nombre,dia,mes,agno=mitupla
print(agno)
