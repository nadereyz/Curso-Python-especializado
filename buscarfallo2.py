#--- GRUPO 2 ---- TOTAL FALLOS: 11

class Pelicula:
    def __init__(self, titulo, director, genero):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.socio = None

    def alquilar(self, socio):
        if self.socio is None:
            self.socio = socio
            print(f"La película '{self.titulo}' ha sido alquilada a {socio.nombre}.")
            return True
        else:
            print(f"La película '{self.titulo}' ya está alquilada a {self.socio.nombre}.")
            return False

    def devolver(self):
        if self.socio is not None:
            print(f"La película '{self.titulo}' ha sido devuelta.")
            self.socio = None
        else:
            print(f"La película '{self.titulo}' no está alquilada.")

class Videoclub:
    def __init__(self):
        self.peliculas_disponibles = []
        self.peliculas_alquiladas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas_disponibles.append(pelicula)
        print(f"La película '{pelicula.titulo}' ha sido añadida al videoclub.")

    def mostrar_peliculas_disponibles(self):
        print("Películas disponibles en el videoclub:")
        for i, pelicula in enumerate(self.peliculas_disponibles, start=1):
            print(f"{i}. Título: {pelicula.titulo}, Director: {pelicula.director}, Género: {pelicula.genero}")

    def alquilar_pelicula(self, indice, socio):
        if 0 < indice <= len(self.peliculas_disponibles):
            pelicula = self.peliculas_disponibles[indice - 1]
            if pelicula.alquilar(socio):
                self.peliculas_disponibles.pop(indice - 1)
                self.peliculas_alquiladas.append(pelicula)
        else:
            print("Índice de película no válido.")

    def devolver_pelicula(self, indice):
        if 0 < indice <= len(self.peliculas_alquiladas):
            pelicula = self.peliculas_alquiladas.pop(indice - 1)
            pelicula.devolver()
            self.peliculas_disponibles.append(pelicula)
        else:
            print("Índice de película no válido.")

class Socio:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear una instancia del videoclub
videoclub = Videoclub()

# Menú de opciones
print("Bienvenido al videoclub.")
print("Seleccione una opción:")
print("1. Agregar una pelicula")
print("2. Mostrar peliculas disponibles")
print("3. Alquilar una pelicula")
print("4. Devolver una pelicula")
print("5. Mostrar peliculas alquiladas")
print("6. Salir")

while True:
    opcion = input("Ingrese el número de la opción seleccionada: ")

    if opcion == '1':
        titulo = input("Ingrese el título de la película: ")
        director = input("Ingrese el director de la película: ")
        genero = input("Ingrese el género de la película: ")
        nueva_pelicula = Pelicula(titulo, director, genero) # tiene que ser con la P mayuscula
        videoclub.agregar_pelicula(nueva_pelicula)
    elif opcion == '2':
        videoclub.mostrar_peliculas_disponibles()
    elif opcion == '3':
        videoclub.mostrar_peliculas_disponibles()
        indice = int(input("Ingrese el número de películas que desea alquilar: "))
        nombre_socio = input("Ingrese su nombre: ")
        socio = Socio(nombre_socio)
        videoclub.alquilar_pelicula(indice, socio)
    elif opcion == '4':
        videoclub.mostrar_peliculas_disponibles() # falta la funcion de mostrar la pelicula alquilada
        indice = int(input("Ingrese el número de la pelicula que desea devolver: "))
        videoclub.devolver_pelicula(indice)
    elif opcion == '5':
        print("Películas prestadas:")
        for i, pelicula in enumerate(videoclub.peliculas_alquiladas, start=1):
            print(f"{i}. Título: {pelicula.titulo}, Director: {pelicula.director}, Género: {pelicula.genero}, Alquilada a: {pelicula.socio.nombre}")
    elif opcion == '6':
        print("Saliendo del programa...")
        break