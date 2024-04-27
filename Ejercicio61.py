class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def __str__(self):
        return f"{self.nombre} es un {self.especie}"

    def sonido(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    total_perros = 0

    def __init__(self, nombre):
        super().__init__(nombre, "perro")
        Perro.total_perros += 1

    def __str__(self):
        return f"{self.nombre} es un {self.especie}, y es muy amigable."

    def sonido(self):
        print(f"{self.nombre} dice: ¡Guau Guau!")

perro1 = Perro("Pepe")
perro2 = Perro("mumu")
perro3 = Perro("jeje")

perros = [perro1, perro2, perro3]
for perro in perros:
    print(perro)
    perro.sonido()

print(f"Total de perros creados: {Perro.total_perros}")
