class Videoclub: #Error de identación,4
    def __init__(self):
        self.catalogo = {} # Son diccionarios, no listas, 21
        self.usuarios = {}

    def agregar_video(self, video):
        self.catalogo= dict(titulo = video)  #NO estoy seguro de si está bien esta corrección,PUEDE HABER UN ERROR OJO
        #self.catalogo[self.titulo] = video 

    def registrar_usuario(self, usuario):
        
        self.catalogo= dict(nombre = usuario)
        #self.usuarios[self.nombre] = usuario # PUEDE HABER UN ERROR OJO


    def prestar_video(self, titulo, nombre_usuario): #Faltan los 2 puntos: , 5
        #Debería ser prestar_video no presta video,21 
        usuario = self.usuarios.get(nombre_usuario) #Estaban cambiados de sitio nombre de usuarío y título,11
        video = self.catalogo.get(titulo) 