class Coche():
  #constructor o edo inicial: son caract comunes con edo inicial especifico, metodo especial que da estado 
  #inicial a los objetos
  #propiedades
  def __init__(self):
    '''asi se declara un metodo constructor y sus variables
    encapsulacion consiste en encapsular o protejer una propiedad para que no pueda ser modificable 
    y es opcional se encapsula nombre.__ es no accesible afuera de la clase pero si dentro y se utiliza 
    tal cual esta pero se puede cambiar a dentro por metodos'''
    self.__largoChasis=250
    self.__anchoChasis=120
    self.__ruedas=4 # 2 __ es un encapsulamiento
    self.__enmarcha=False
  #comportamientos o métodos
  def arrancar(self,arrancamos):
    #metodo es una funcion especial que pertenece a una clase
    #self hace referencia al objeto pertenenciente a la clase o this en c++ o en java
    self.__enmarcha=arrancamos
    #lo de abajo es lo mismo que poner self.enmarcha==true
    if(self.__enmarcha):
      chequeo=self.__chequeo_interno()
    if(self.__enmarcha and chequeo):
      return "El coche esta en marcha"
    elif (self.__enmarcha and chequeo==False):
      return "Algo anda mal en el chequeo no podemos arrancar "
    else:
      return "El coche esta parado"

  def estado(self):
    print("el coche tiene ",self.__ruedas, " ruedas. Un ancho de ",self.__anchoChasis," y un largo de ", 
      self.__largoChasis)

  def __chequeo_interno(self): #encapsulaicon de metodo
    print("realizando chequeo interno")
    self.gasolina="ok"
    self.aceite="ok"
    self.puertas="cerradas"
    if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
      return True
    else:
      return False 
    
miCoche=Coche() #creación de objeto o instanciar clase
'''print("El largo del coche es: ", miCoche.largoChasis)#acceso a propiedades
print("El coche tiene ", miCoche.ruedas , " ruedas")'''
#lo de abajo es una llamada al metodo que se define por estar en una clase
print(miCoche.arrancar(True))
miCoche.estado()
print("-----------A continuacion creamos un segundo objeto---------------")
miCoche2=Coche()
'''print("El largo del coche es: ", miCoche2.largoChasis)
print("El coche tiene ", miCoche2.ruedas , " ruedas")''' 
print(miCoche2.arrancar(False))
#micoche2.__ruedas=5 # con el punto se modifican propiedades y si esta encapsulado no hay cambios
miCoche2.estado()
#print(micoche.chequeo_interno())# intentalo y no va ser accesible desde fuera
#encapsulacion: protege a las propiedades para que nadie las modifique y solo accesible en la clase y ademas 
#se usara con los 2 guiones bajos

#hasattr funcion que nos dice si tiene el atributo
# setattr sirve como setter
# delattr borra atributo