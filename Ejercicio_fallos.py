class Video:
    def __init__(self, titulo, director, genero, duracion):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.duracion = duracion
        self.disponible = True

    def __repr__(self):
        return f"Video(titulo='{self.titulo}', director='{self.director}', genero='{self.genero}', duracion={self.duracion})"

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = set()
        self.reservas = set()

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}')"

class Videoclub:
    def __init__(self):
        self.catalogo = [] # dentro de este def tiene que ser (), no []
        self.usuarios = [] # dentro de este def tiene que ser (), no []

    def agregar_video(self, video):
        self.catalogo[self.titulo] = video # tiene que ser video.titulo

    def registrar_usuario(self, usuario):
        self.usuarios[self.nombre] = usuario  # tiene que ser usuario.nombre

    def presta_video(self, titulo, nombre_usuario): # tiene que ser prestar_video
        usuario = self.usuarios.get(titulo) # aqui dentro de () tiene que ser nombre_usuario
        video = self.catalogo.get(nombre_usuario) # aqui dentro de () tiene que ser titulo 

        if usuario and video and video.disponible:
            usuario.prestamos.add(titulo)
            video.disponible = False
            return f"Video '{titulo}' prestado a {nombre_usuario}."
        return "Préstamo no disponible."

    def reservar_video(self, titulo, nombre_usuario):
        usuario = self.usuarios.get(nombre_usuario)
        video = self.catalogo.get(titulo)
        if usuario and video and not video.disponible:
            usuario.reservas.add(titulo)
            return f"Video '{titulo}' reservado por {nombre_usuario}."
        return "Reserva no disponible."

    def devolver_video(self, titulo, nombre_usuario):
        usuario = self.usuarios.get(nombre_usuario)
        video = self.catalogo.get(titulo)
        if usuario and video and titulo in usuario.prestamos:
            usuario.prestamos.remove(titulo)
            video.disponible = True
            return f"Video '{titulo}' devuelto por {nombre_usuario}."
        return "Devolución no válida."

# Creación de la biblioteca del videoclub
biblioteca = Videoclub()

# Agregar videos al catálogo
biblioteca.agregar_video(Video("El Padrino", "Francis Ford Coppola", "Crimen", 175))
biblioteca.agregar_video(Video("La La Land", "Damien Chazelle", "Musical", 128))

# Registrar usuarios
biblioteca.registrar_usuario(Usuario("Juan"))
biblioteca.registrar_usuario(Usuario("Ana"))

# Prestar un video
print(biblioteca.prestar_video("El Padrino", "Juan"))

# Reservar un video
print(biblioteca.reservar_video("El Padrino", "Ana"))

# Devolver un video
print(biblioteca.devolver_video("El Padrino", "Juan"))

# Intentar reservar un video disponible (debería fallar)
print(biblioteca.reservar_video("La La Land", "Juan"))