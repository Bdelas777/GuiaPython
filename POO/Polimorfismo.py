class Coche():
	def desplazamiento(self):
		print("Me desplazo en cuatro ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo en dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo en seis ruedas")

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()
#polimorfismo es tener llamado a un metodo igual en cada clase 
'''
MiVehiculo=Moto()
MiVehiculo.desplazamiento()

MiVehiculo2=Coche()
MiVehiculo2.desplazamiento()

MiVehiculo3=Camion()
MiVehiculo3.desplazamiento()'''
miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo)# distingue por el objeto 
#Poliforfismo Un objeto puede cambiar de forma y comportamiento dependiendo del contexto que lo van utilizar