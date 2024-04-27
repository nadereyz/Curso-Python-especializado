class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.usuario = ""  # Eso lo pongo vacio para saber que no esta prestado. tambien sirve para None

    def prestar(self, usuario):
        if self.usuario == "":  # con if lo que hago es comprobar si el libro esta prestado al usuario o no
            self.usuario = usuario
            return True
        return False

    def devolver(self):
        if self.usuario != "":  # aqui compruebo si esta prestado no
            self.usuario = ""
            return True
        return False

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = [] # aqui inicializo las 2 listas que seria disponible y prestado
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro) # aqui cada vez que utilizo la funcion pues voy agregando.

    def mostrar_libros_disponibles(self): # aqui lo que hace es recorrer la lista y mostrar los libros disponibles
        print("Libros disponible:")
        for libro in self.libros_disponibles:
            print(f"{libro.titulo} de {libro.autor} -  El Genero: {libro.genero}")

    def prestar_libro(self, titulo, usuario):
        for libro in self.libros_disponibles: # Aqui lo que hago es recorrer el for dentro de libros disponibles y si el titulo es igual a titulo que es decir que existe, pues me va a prestar, 
            #y despues comprueba al usuario y le va a prestar el libro
            if libro.titulo == titulo:
                if libro.prestar(usuario):
                    self.libros_disponibles.remove(libro) #si hay algun libro disponible pues se eliminara (prestando)
                    self.libros_prestados.append(libro) # y se agregara a la lista de libros prestados
                    return True
        return False

    def devolver_libro(self, titulo):
        for libro in self.libros_prestados:
            if libro.titulo == titulo:
                if libro.devolver():
                    self.libros_prestados.remove(libro)
                    self.libros_disponibles.append(libro)
                    return True
        return False

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

def main():
    biblioteca_dav = Biblioteca()
    usuario = Usuario("Alejandra Espinosa") 

    biblioteca_dav.agregar_libro(Libro("Python", "Alejandra Espinosa", "Ciencia Ficcion"))
    biblioteca_dav.agregar_libro(Libro("El Asesino Mentor", "Pepito Memito", "Terror"))

    biblioteca_dav.mostrar_libros_disponibles()

    
    if biblioteca_dav.prestar_libro("Python", usuario.nombre):
        print(f"\nEl libro 'Python' ha sido prestado a {usuario.nombre}.")
    else:
        print("\nEl libro 'Python' no está disponible.")

    
    biblioteca_dav.mostrar_libros_disponibles()

   
    if biblioteca_dav.devolver_libro("Python"):  # Devolver un libro
        print(f"\nEl libro 'Python' ha sido devuelto.")
    else:
        print("\nError al intentar devolver el libro.")

    
     #mostrar despues de devolver
    biblioteca_dav.mostrar_libros_disponibles()

main()
