class Persona():
	def __init__(self,nombre,edad,lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def descripcion(self):
		print("Nombre: ",self.nombre," Edad: ",self.edad," Lugar de residencia: ",self.lugar_residencia  )
		
class Empleado(Persona):
	def __init__(self, salario, antiguedad,nombre_empleado,edad_empleado,lugar_residencia_empleado):
		#super funcion que llama al metodo de la clase padre
		super().__init__(nombre_empleado,edad_empleado,lugar_residencia_empleado)
		#Ejecuta enteramente el metodo init de la clase padre 
		self.salario=salario
		self.antiguedad=antiguedad
	def descripcion(self):
		super().descripcion()#modifica el metodo de arriba
		print(" Salario: ", self.salario," Antiguedad: ", self.antiguedad)

#principio de sustitucion; es siempre un/a
Antonio=Empleado(1500,15,"Antonio",55,"España",)
Antonio.descripcion()
#isinstance nos informa si un objeto forma parte de una instancia determinada
print(isinstance(Antonio,Persona))
