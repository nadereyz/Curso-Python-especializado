biblioteca = {
    "Titulo 1": 10,
    "Titulo 2": 7,
    "Titulo 3": 5,
    "Titulo 4": 6,
    "Titulo 5": 8
}

def prestar_libro(existen, cantidad):
    """
    Este es una prueba
        *if y def
            * no se que mas.  
                - que paso pasoooo 
                    1. Si la cantidad a prestar es menor o igual a cero:
                    1.1 Devuelve un mensaje de error indicando que no se puede prestar libros negativos o ceros.
                    1.2 no se que mas
                        2.1  si el libro existe en existen:
    """
    help(prestar_libro)
    if existen in biblioteca:
        disponibles = biblioteca[existen]
        if disponibles >= cantidad:
            biblioteca[existen] -= cantidad
            print(f"Se prestado {cantidad} ejemplares del libro ->{existen}<-")
        else:
            print(f"Lo siento, no hay mas libros  ->{existen}<-")
    else:
        print(f"El libro  ->{existen} -> no existe")

def devolver_libro(titulo, cantidad):
    if titulo in biblioteca:
        biblioteca[titulo] += cantidad
        print(f"Se han devuelto {cantidad} ejemplares del libro  ->{titulo}<-")
    else:
        print(f"El libro  ->{titulo}<- no existe")

def ver_inventario():
    print("Inventario de la biblioteca:")
    for libro, cantidad in biblioteca.items():
        print(f"---> {libro}: {cantidad} ejemplares disponibles")

print("--- Préstamo de libros ---")
prestar_libro("Titulo 1", 3)
prestar_libro("Titulo 3", 7)

print("\n--- Devolución de libros ---")
devolver_libro("Titulo 1", 2)
devolver_libro("Titulo 3", 5)

print("\n--- Inventario actual ---")
ver_inventario()

