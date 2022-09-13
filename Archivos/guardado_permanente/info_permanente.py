'''
Este programa es para ver el guardado permanente
este codigo es util para reutilizarlo en el futuro
'''
import pickle 

class Persona:
	def __init__(self,nombre,genero,edad):# el constructor
		self.nombre=nombre
		self.genero=genero
		self.edad=edad	
		print("Se creado un persona nueva con el nombre de ", self.nombre)
    #metodo de abajo convierte en string
	def __str__(self):#convierte en cadena de texto la informacion de un objeto
	    return "{} {} {}".format(self.nombre, self.genero, self.edad)#recuerda que format da un  formato

class ListaPersonas:

	personas=[]

	def __init__(self):

		listaDePersonas=open("ficheroExterno","ab+")#agregar infromacion binaria
		listaDePersonas.seek(0)#seek nos pone la informacion en un orden 

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo ".format(len(self.personas)))#aqui usamos format y len porque
			#len cuenta el numero de personas que han pasado y format dice la posicion que lo va a poner

		except:
			print("El fichero esta vacio")
		
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self,p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")#write byte
		pickle.dump(self.personas, listaDePersonas)
		del(listaDePersonas)

	def MostrarInformacionEnFicheroExterno(self):
		print("La informacion del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()
nombre=input("Introduce el nombre de la persona: ")
sexo=input("Introduce el sexo de la persona: ")
edad=int(input("Introduce la edad de la persona: "))
persona=Persona(nombre,sexo,edad)
miLista.agregarPersonas(persona)
miLista.MostrarInformacionEnFicheroExterno()

'''ejemplo de chequeo al principio
p=Persona("Sandra","Femenino",22)
milista.agregar_personas(p)
milista.lecturafichero()'''

#p=Persona("Juan","Masculino",32)
#milista.agregar_personas(p)

#p=Persona("Ana","Femenino",18)
#milista.agregar_personas(p)

#milista.mostrar_personas()'''
