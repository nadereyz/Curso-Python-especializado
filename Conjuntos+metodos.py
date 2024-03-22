#*************** CONJUNTOS / SETS **********************

#Bucle For para iterar sobre los elementos de mi set/conjunto
conjunto_iterable = {5, 6, 7, 8}
for elemento in conjunto_iterable:
    print(elemento)
print(conjunto_iterable)

conjunto_iterable_dos = set([3, 4, 5, 6])
for elemento_dos in conjunto_iterable_dos:
    print(elemento_dos)

#Comprobar si un valor esta presente en mi conjunto
presente_set = {"rojo", "azul", "verde"}
color_seleccionado = str(input("Introduce un color:\n"))
print(f"¿Esta el color {color_seleccionado} en mi set?",color_seleccionado in presente_set)


#-----------------MÉTODOS DE SETS/CONJUNTOS---------------

#Método add(): Agregar un elemento al conjunto. Si el elemento que yo agrego YA EXISTE en el conjunto, no realizará ningún cambio. 
conjunto_aniade = {1, 2, 3}
conjunto_aniade.add(4)
conjunto_aniade.add(2)
print(conjunto_aniade)

#Método remove(): Eliminar un elemento de mi conjunto pasándole el valor del elemento por argumentos. Si el elemento no está en mi conjunto, me devolverá un error. 
conjunto_borrar = {1, 2, 3}
conjunto_borrar.remove(2)
#conjunto_borrar.remove(4) #KeyError
print(conjunto_borrar)


#Método add(): Agregar un elemento al conjunto. Si el elemento que yo agrego YA EXISTE en el conjunto, no realizará ningún cambio. 
conjunto_aniade = {1, 2, 3}
conjunto_aniade.add(4)
conjunto_aniade.add(2)
print(conjunto_aniade)

#Método remove(): Eliminar un elemento de mi conjunto pasándole el valor del elemento por argumentos. Si el elemento no está en mi conjunto, me devolverá un error. 
conjunto_borrar = {1, 2, 3}
conjunto_borrar.remove(2)
#conjunto_borrar.remove(4) #KeyError
print(conjunto_borrar)

#Método discard(): Eliminar un elemento de mi conjunto pasándole el valor del elemento por argumentos. Si el elemento no está en mi conjunto, NO REALIZA NINGUN CAMBIO Y TAMPOCO ME GENERA UN ERROR. 
conjunto_descartar = {1, 2, 3}
conjunto_descartar.discard(2)
conjunto_descartar.discard(4) #--> No me devuelve un KeyError
print(conjunto_descartar)

 #Método clear(): Elimina TODOS los elementos de mi conjunto
conjunto_limpiar = {1, 2, 3, 4}
conjunto_limpiar.clear()
print(conjunto_limpiar) #Devuelve set() --> Un conjunto/set vacio

#Método len(): Devuelve la cantidad de elementos que están presentes en mi conjunto/set.
conjunto_longitud = {1, 2, 3, 4, 5, 7, 7, 6, 5, 6}
print("El número de elementos en mi conjunto es:", len(conjunto_longitud))
longitud = len(conjunto_longitud)
print("El número de elementos en mi conjunto es:", longitud)

#Método split(): se utiliza EN CADENAS DE TEXTO para dividirlas en una lista de subcadenas. Podemos incluir el separador como parámetro y va a representar el caracter o la cadena que se utilizará como separador. Es opcional. Si no lo especificamos, el método split() va a tomar como referencia los espacios en blanco entre las palabras como separador por defecto.
#Separador "-"
frase_uno = "Hola-que tal"
lista_palabras_uno = frase_uno.split("-")
print("Lista de palabras separadas por guión: ", lista_palabras_uno)
#Separador ","
frase_dos = "Hola,que,tal"
lista_palabras_dos = frase_dos.split(",")
print("Lista de palabras separadas por comas: ", lista_palabras_dos)
#Sin separador
frase_tres = "Hola que tal"
lista_palabras_tres = frase_tres.split()
print("Lista de palabras sin separador: ", lista_palabras_tres)

print("-------------")

conjunto_a_actualizar = {1, 2, 3, 4}
lista_a_agregar = [4, 5, 6]
conjunto_a_actualizar.update(lista_a_agregar)
print("Conjunto actualizado con la lista:", conjunto_a_actualizar)
