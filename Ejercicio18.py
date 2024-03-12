
edad1 = int(input("escribe la edad del primer familiar: "))
edad2 = int(input("escribe la edad del segundo familiar: "))
edad3 = int(input("escribe la edad del tercer familiar: "))
edad4 = int(input("escribe la edad del cuarto familiar: "))

lista_edades = [edad1, edad2, edad3, edad4]

# (NO TE OLVIDES DE LA MENOR A MAYOR!)
lista_edades_ascendente_sort = sorted(lista_edades)
lista_edades_ascendente_sorted = lista_edades.copy()
lista_edades_ascendente_sorted.sort()

# (NO TE OLVIDES DE MAYOR A MENOR)
lista_edades_descendente_sort = lista_edades.copy()
lista_edades_descendente_sort.sort(reverse=True)
lista_edades_descendente_sorted = sorted(lista_edades, reverse=True)

print("Toda la informacion que has escrito antes son:", lista_edades)
print("De forma Ascendentemente:", lista_edades_ascendente_sort, lista_edades_ascendente_sorted)
print("De forma Descendentemente:")
print(lista_edades_descendente_sort, lista_edades_descendente_sorted)
