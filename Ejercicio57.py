# CONTINUAMOS CON EL EJEMPLO BIBLIOTECA

class Libro:
    #Este atributo de clase hace referencia a todas las instancias que se creen de esta misma clase. Este valor es común para todas las instancias. 
    cantidad_libros_en_biblioteca = 0
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        #Cada vez que cree una instancia de la clase Linro, quiero que la cantidad de libros en biblioteca se incremente en 1
        Libro.cantidad_libros_en_biblioteca += 1
    #Formateamos la salida del objeto para que en vez de mostrarnos la clase a la que pertenece y su ubicación en la memoria, nos muestre la salida con el formato que necesitamos, más legible y fácilmente comprensible.
    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor}"
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de paginas: {self.paginas}\n")

#Creamos dos objetos de la clase Libro      
libro_uno = Libro("El Alquimista", "Paulo Coehlo", 149)
libro_dos = Libro("Juan Salvador Gaviota", "Nader El Yacoubi", 239)

#Modifico el valor de un atributo en una instancia específica
libro_uno.titulo = "Nuevo valor para el título del libro 1"

#Mostrar la información de las instancias que he creado
print("Información libro 1:\n")
libro_uno.mostrar_info()

print("Información libro 2:\n")
libro_dos.mostrar_info()

#Mostrar la cantidad actual de libros en mi biblioteca
print(f"La cantidad actual de libros es: {Libro.cantidad_libros_en_biblioteca}")

#Creo un nuevo objeto de la clase Libro
libro_tres = Libro("Python essentials", "Guido Van Rossum", 698)

#Mostrar la cantidad actual de libros en mi biblioteca
print(f"La cantidad actual de libros es: {Libro.cantidad_libros_en_biblioteca}")

#Creamos una lista 'biblioteca' que almacene los objetos de la clase Libro
biblioteca = [libro_uno, libro_dos, libro_tres]
#Iteramos sobre cada uno de los elementos de la lista 'biblioteca', imprimiéndolos en pantalla. 
for libro in biblioteca:
    print(libro)