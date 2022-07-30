class Vehiculos():
	#caracteristicas comunes y constructor
	def __init__(self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
		#comportamientos o metodos
	def arrancar(self):
		self.enmarcha=True
	def acelerar(self):
		self.acelera=True
	def frener(self):
		self.frena=True
	def estado(self):
		print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEsta arrancado: ", self.enmarcha,
			"\nEsta acelerando: ",self.acelera,"\nEsta frenando: ", self.frena)
#Como heredar checalo abajo
class Furgoneta(Vehiculos):
	def cargar(self,carga):
		self.cargado=carga
		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta esta vacía"
#Recuerda si hay un return siempre usa un print	
class moto(Vehiculos):#Se hereda poniendo en el parentesis
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"
		#sobreescrimiento de metodos,debe ser same nombre que clase padre y mismo numero de parametros
	def estado(self):
		print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEsta arrancado: ", self.enmarcha,
			"\nEsta acelerando: ",self.acelera,"\nEsta frenando: ", self.frena,"\n", self.hcaballito)

class VehiculosElectricos(Vehiculos):
	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.Autonomia=100
	def cargar_energia(self):
		self.cargando=True

class BicicletaElectrica(VehiculosElectricos,Vehiculos):
	#herencia multiple como se muestra ahi, se hereda todo de ambas clases
	pass

#jerarquia de herencia: hereda el ultimo metodo modificado
'''
marca=input("Introduzca la marca: ")
modelo=input("Introduzca el modelo: ")'''

miMoto=moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.cargar(True))

mibici=BicicletaElectrica("BiciNew","Azul")#la clase hereda el constructor de la primera clase
#en la herencia multiple 
