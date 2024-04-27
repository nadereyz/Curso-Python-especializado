print("\nBIENVENIDO A LA AGENCIA DE SALUD DE RAQUELITA 🦊")
print("/" * 45)

class Personas:
    comportamiento1 = "nacer"   # Estos son los atributos ESTÁTICOS
    comportamiento2 = "crecer"
    comportamiento3 = "morir"
    
    def __init__(self, nombre, edad, altura, peso):  # Estos son los atributos DINÁMICOS
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
    
    def establecer_nombre(self, nombre: str):  # Establecer los nombres
        self.nombre = nombre
        
    def obtener_nombre(self):  # Devolverá el contenido almacenado
        return self.nombre
    
    def establecer_edad(self, edad: int):
        self.edad = edad
    
    def obtener_edad(self):
        return self.edad
    
    def establecer_altura(self, altura: float):
        self.altura = altura
    
    def obtener_altura(self):
        return self.altura
    
    def establecer_peso(self, peso: float):
        self.peso = peso
    
    def obtener_peso(self):
        return self.peso

# Pedir los valores
nombre = input("Introduce nombre: ")
edad1 = int(input("Introduce edad: "))
altura1 = float(input("Introduce altura: "))
peso1 = float(input("Introduce peso: "))

# Asignar los valores   
 
persona1 = Personas(nombre, edad1, altura1, peso1)

# Imprimir los resultados
print("\nResultados:")
print("Nombre:", persona1.obtener_nombre()) 
print("Edad:", persona1.obtener_edad())
print("Altura:", persona1.obtener_altura())
print("Peso:", persona1.obtener_peso())

print("\nEso es todo amigos! by Rae👻")
