mi_lista_for = ["Hola", "Adios", 1, 2, 3, "Hola"]

for element in mi_lista_for:
    print(element)
    mi_lista_for.remove("Hola")

print("Lista actualizada después de eliminar 'Hola':", mi_lista_for)