# CONTINUAMOS CON EL EJEMPLO BIBLIOTECA

class Libro:
    #Este atributo de clase hace referencia a todas las instancias que se creen de esta misma clase. Este valor es común para todas las instancias. 
    cantidad_libros_en_biblioteca = 0
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        #Cada vez que cree una instancia de la clase Libro, quiero que la cantidad de libros en biblioteca se incremente en 1
        Libro.cantidad_libros_en_biblioteca += 1
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de paginas: {self.paginas}\n")

while True:
    agregar = input("Añadir nuevolibro?  (si o no): ")
    if agregar.lower() == 'si':
        titulo = str(input("Pon el tiutlo del libro: "))
        autor = str(input("Pon el autor del libro: "))
        paginas = int(input("Cuantas paginas del libro: "))
        libro = Libro(titulo, autor, paginas)
        libro.mostrar_info()  
    elif agregar.lower() == 'nno':
        break
    else:
        print("Por favor, ingrese 's' para sí o 'n' para no.")

#Mostrar la cantidad actual de libros en mi biblioteca
print(f"La cantidad actual de libros es: {Libro.cantidad_libros_en_biblioteca}")

