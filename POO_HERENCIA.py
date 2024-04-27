





# POO - HERENCIA ****************************************
""" 
· Podemos crear nuevas clases a partir de clases ya existentes. 
· Nos permite que una clase (subclase o clase derivada) herede tanto atributos como métodos de otra clase (superclase o clase base)
· La herencia facilita la reutilización del código y la creación de jerarquías de clases --> Tratamos de promover en todo caso un diseño modular y extensible

"""
#Defino una clase --> SUPERCLASE O CLASE BASE
class Animal:
    tipo = "Mamífero"
    bigotes = "largos y sensibles"
    #Métodos
    pass

#Defino una clase --> SUBCLASE O CLASE DERIVADA
class Perro(Animal):
    #hereda tipo = "Mamífero"
    bigotes = "" #Puedo sobreescribir un atributo heredado de la clase base.
    sonido = "ladrar"
    pass

class Chihuahua(Perro):
    #hereda tipo = "Mamífero"
    #hereda sonido = "ladrar"
    #hereda bigotes = ""
    pass

class Gato(Animal):
    #hereda tipo = "Mamífero"
    #hereda bigotes = "largos y sensibles"
    sonido = "maullar"
    pass

#EJEMPLO 1 de CLASES HEREDADAS

#Definimos una CLASE BASE Vehículo que contenga atributos de instancia y métodos de instancia
class Vehiculo:
    
    __slots__ = ['marca', 'modelo'] # 1. Limitación de atributos; 2. Reducción de la sobrecarga de memoria
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

        
    def mostrar_informacion(self):
        print(f"Marca: {self.marca} - Modelo {self.modelo}")

#Definimos una CLASE DERIVADA Coche, que herede los atributos de instancia de la clase base y además añada nuevos atributos. 
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo) #Llamamos al constructor de la clase base para inicializar los atributos de la propia clase. La función super() me permite acceder a los métodos (de clase y de instancia) de la clase padre desde una de sus clases hijas. 
        self.color = color
    
    """ 
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    """
    
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Color: {self.color}")
        
coche_uno = Coche("Land Rover", "freelander", "gris")
#coche_uno.mostrar_informacion()

"""OTROS ATRIBUTOS ESPECIALES PARA TRABAJAR CON CLASES HEREDADAS"""

#ATRIBUTO ESPECIAL __base__: Proporciona una referencia de la clase de la cual es derivada. Es decir, me dice quien es su clase padre. En el caso de que no tenga una clase padre, nos remite a un valor object (la base de todas las clases en Python)

""" print(Chihuahua.__base__)
print(Perro.__base__)
print(Animal.__base__) """


#ATRIBUTO ESPECIAL __subclasses__(): Obtengo una lista de todas las clases derivadas de una clase base.
""" print(Animal.__subclasses__())
print(Perro.__subclasses__()) """


#ATRIBUTO ESPECIAL __mro__: Method Resolution Order (Orden de Resolución de Métodos). Devuelve una tupla que nos muestra el orden en el que las clases se van a buscar en mi jerarquía de clases a la hora de resolver atributos y métodos en una instancia. 

print(Chihuahua.__mro__)
print("*" * 100)
print(Perro.__mro__)
print("*" * 100)
print(Animal.__mro__)
print("*" * 100)

#Ejemplo de uso de __mro__:

class A:
    """Descripción:
     Esta es la clase de ejemplo A
    """
    def __init__(self, atr_uno, atr_dos):
        self.atr_uno = atr_uno
        self.atr_dos = atr_dos
    
    def metodo_uno():
        return print("Soy el método uno")
   
class B(A):
    """comentario"""

class C(B):
    pass

class D(C):
    """Descripción:
    Esta es la descripción

    Argumentos de la función: 
        C (_type_): _description_
    """
    def metodo_tres(): 
        return print("Soy el método uno")

print(D.__doc__)
print(D.__dict__)
print(D.__mro__)
print(C.__mro__)
print(B.__mro__)
print(A.__mro__)
    

"""OTROS ATRIBUTOS ESPECIALES COMUNES"""

#Atributo __doc__: Este atributo va a devolver toda la documentación asociada con una clase.
class Documentacion:
    """
    Nombre de la clase: Documentacion
        Descripción:
        Esta clase se ha definido para documentar y explicar el uso del atributo especial __doc__
    """
    pass

print(Documentacion.__doc__)

#Atributo __dict__: Este atributo nos devuelve un diccionario que contiene los atributos de la instancia de la clase, incluídos los métodos. CLAVE (nombres de los atributos) - VALOR (valores de los atributos)

print(Perro.__dict__) #Nos muestra un diccionario que contiene los atributos de la instancia de la clases dada, en este caso, Perro.

print("Este documento recoge la clase Animal, y las clases derivadas de la class Animal.\nINDICE\n \n- Class Animal" , Animal.__mro__ , "\n Atributos que contiene:", Animal.__dict__, "\n\n   - Class Perro", Perro.__mro__ , "\n\n        -Class Chihuahua" , Chihuahua.__mro__ ,  "\n        Atributos que contiene:", Chihuahua.__dict__, "\n\n  - Class Gato" , Gato.__mro__ , "\n     Atributos que contiene:", Gato.__dict__)

print("Clase: A")
print("    · Documentación:")
print("    ", A.__doc__)
print("    · Métodos y atributos:")
print("    ", A.__dict__)
print("    · Jerarquía de clases:")
print("    ", A.__mro__)

""" A partir del ejemplo de las clases A, B, C y D vas a mostrar la documentación de estas clases, la jerarquía de clases de las que derivan y además los atrubitos de instancia y los métodos de la clase"""