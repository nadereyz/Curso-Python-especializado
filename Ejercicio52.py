class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def Presentar(self):
        print("Hola, soy ", self.nombre, " y tengo ", self.edad, " años.")
nombre = input("Introduce el nombre de la persona: ")
edad = int(input("Introduce la edad de la persona: "))
persona = Persona(nombre, edad)

persona.Presentar()