
#-- 11 FALLOS -- 
class Pelicula:
    def __init__(self, titulo, director, genero):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.usuario = None # tiene que ser None ya que si los demas tiene puesto None pues aqui tambien.

    def prestar(self, usuario):
        if self.usuario is None:
            self.usuario = usuario
            print(f"La película {self.titulo} ha sido prestada a {self.usuario.nombre}.") # falta el self.titulo y el self.usuario.nombre
            return True
        else:
            print(f"La película '{self.titulo}' ya está prestada a {self.usuario.nombre}.") # falta el self.usuario.nombre
            return False

    def devolver(self):
        if self.usuario is not None:
            print(f"La película '{self.titulo}' ha sido devuelta.")
            self.usuario = None
        else:
            print(f"La película '{self.titulo}' no está prestada.")

class Videoclub:
    def __init__(self): # tiene que ser __init__
        self.peliculas_disponibles = []
        self.peliculas_prestadas = [] # tiene que ser []

    def agregar_pelicula(self, pelicula):
        self.peliculas_disponibles.append(pelicula) # falta la s
        print(f"La pelicula '{pelicula.titulo}' ha sido añadida al videoclub.")

    def mostrar_peliculas_disponibles(self):
        print("Peliculas disponibles en el videoclub:")
        for i, pelicula in enumerate(self.peliculas_disponibles):
            print(f"{i + 1}. Título: {pelicula.titulo}, Director: {pelicula.director}, Género: {pelicula.genero}") # en vez de j tiene que ser i y añadir + 1

    def prestar_pelicula(self, indice, usuario):
        if 0 < indice <= len(self.peliculas_disponibles):
            pelicula = self.peliculas_disponibles[indice - 1] # tiene que restar dentro de indice - 1 
            if pelicula.prestar(usuario):
                self.peliculas_disponibles.pop(indice - 1)
                self.peliculas_prestadas.append(pelicula)
        else:
            print("Índice de película no válida.")

    def devolver_pelicula(self, indice):
        if 0 < indice <= len(self.peliculas_prestadas):
            pelicula = self.peliculas_prestadas.pop(indice - 1)
            pelicula.devolver()
            self.peliculas_disponibles.append(pelicula)
        else:
            print("Índice de película no válida.")

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear una instancia de la biblioteca
videoclub = Videoclub()

# Menú de opciones
print("Bienvenido al Videoclub.")
print("Seleccione una opción:")
print("1. Agregar una película")
print("2. Mostrar películas disponibles")
print("3. Prestar una película")
print("4. Devolver una película")
print("5. Mostrar películas prestadas")
print("6. Salir")

while True:
    opcion = input("Ingrese el número de la opción seleccionada: ")

    if opcion == '1':
        titulo = input("Ingrese el título de la película: ")
        director = input("Ingrese el director de la película: ")
        genero = input("Ingrese el género de la película: ")
        nueva_pelicula = Pelicula(titulo, director, genero)
        videoclub.agregar_pelicula(nueva_pelicula)
    elif opcion == '2':
        videoclub.mostrar_peliculas_disponibles()
    elif opcion == '3':
        videoclub.mostrar_peliculas_disponibles()
        indice = int(input("Ingrese el número de la película que desea prestar: "))
        nombre_usuario = input("Ingrese su nombre: ")
        usuario = Usuario(nombre_usuario)
        videoclub.prestar_pelicula(indice, usuario)
    elif opcion == '4': # falta poner '4'
        videoclub.mostrar_peliculas_disponibles()
        indice = int(input("Ingrese el número de la película que desea devolver: "))
        videoclub.devolver_pelicula(indice)
    elif opcion == '5':
        print("Películas prestadas:")
        for i, pelicula in enumerate(videoclub.peliculas_prestadas, start=1):
            print(f"{i}. Título: {pelicula.titulo}, Director: {pelicula.director}, Género: {pelicula.genero}, Prestada a: {pelicula.usuario.nombre}") # error de pelicula.usuario.nombre 
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")