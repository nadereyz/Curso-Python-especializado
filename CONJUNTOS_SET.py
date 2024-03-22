
#*************** CONJUNTOS / SETS **********************
"""Colecciones de datos no ordenadas, a las que no voy a poder acceder a los elementos a través de su index y cuya sintaxis se construye utilizando el símbolo "{}". Admite cualquier tipo de datos. No pueden contener elementos duplicados. No aplica una forma específica para acceder a los elementos.
CARACTERÍSTICAS FUNDAMENTALES:
· Elementos únicos: No pueden contener duplicados, ni otros conjuntos directamente, ya que los elementos de un conjunto deben ser inmutables, y los conjuntos son mutables.
· No ordenados
· Mutables
· Sintaxis de creacción: {} & set() 
· Admite la mayoría de tipos de dato, dentro de las colecciones de datos solo admitirá tuplas. Además, será ilógico incluir valores booleanos dentro de nuestro conjunto.
    logico = True, False #Puedo acceder por index y es inmutable
    ilogico = {True, False} #No puedo acceder por index y además no mantiene el orden de insercción
"""

"""
mi_primer_conjunto = {"elemento1", "elemento2", 3, 4, 4.1, True} #Se crea utilizando las {}
print(mi_primer_conjunto)
print("Este es mi primer conjunto:", mi_primer_conjunto)

mi_primer_set = set([2, 5, 6, 2, 3, 4]) #También podemos crear conjuntos utilizando el método de constructor set()
print(mi_primer_set) 

conjunto_y_tupla = {1, 2, 3, (4, 5)}
print("Conjunto y tupla:", conjunto_y_tupla)

#------------OPERACIONES CON CONJUNTOS-----------------
#Conjuntos de referencia
conjunto_uno = {1, 2, 3, 4, 5} 
conjunto_dos = {5, 2, 8, 4, 0} 

#Union (|) o union(): Une los conjuntos, sin respetar el orden de inserción y también pudiendo mezclar los valores de ambos conjuntos en la salida del nuevo conjunto creado. Devuelve un nuevo conjunto que contenga todos los elementos que estén en al menos 1 conjunto.
union = conjunto_uno | conjunto_dos
union_dos = conjunto_uno.union(conjunto_dos)
print("Unión con tubería: ", union, "\nUnión con método union()", union_dos)

#Intersección (&) o .intersection(): Devuelve un nuevo conjunto que contiene todos los elementos que estan en los dos conjuntos.
interseccion = conjunto_dos & conjunto_uno
interseccion_dos = conjunto_uno.intersection(conjunto_dos)
print("Interseccion con &:", interseccion, "\nIntersección con método intersection():", interseccion_dos)

#Diferencia (-) o difference(): Devuelve un nuevo conjunto que contiene los elementos que están en el primer conjunto, pero no en el segundo.
diferencia = conjunto_dos - conjunto_uno
diferencia_dos = conjunto_uno.difference(conjunto_dos)
print("Diferencia entre conjuntos:\n Diferencia con - :\n", diferencia,"\nDiferencia con método difference():\n", diferencia_dos)

#Diferencia simétrica (^) o symmetric_difference(): Devuelve un nuevo conjunto que contenga todos los elementos que están en alguno de los conjuntos, pero no en ambos.
diferencia_simetrica = conjunto_uno ^ conjunto_dos
diferencia_simetrica_dos =  conjunto_dos.symmetric_difference(conjunto_uno)
print("Diferencia simétrica con ^:", diferencia_simetrica,"\nDiferencia simétrica con método symmetric_difference()", diferencia_simetrica_dos)

#Subconjunto issubset(): Evaluamos si todos los elementos del primer conjunto están presentes en el segundo conjunto. Devuelve True si todos los elementos del primer están en el segundo y False de lo contrario.
conjunto_tres = {1, 2, 3, 4, 5} 
conjunto_cuatro = {1, 2, 3, 4, 5, 6, 7, 8} 
subconjunto = conjunto_tres.issubset(conjunto_cuatro)
print("Todos los valores del primer conjunto están presentes en el segundo:", subconjunto) #True

#Superconjunto issuperset(): Evaluar si todos los elementos del segundo conjunto estan presentes en el primero. Devuelve True si todos los elementos del segundo conjunto están presentes en el primero
superconjunto = conjunto_tres.issuperset(conjunto_cuatro)
valores_diferentes = conjunto_cuatro - conjunto_tres
print("Todos los valores del segundo conjunto están presentes en el primero:", superconjunto, "porque al primer conjunto le faltan estos valores:", valores_diferentes) 

"""
"""INCISO
Función: Bloque de código que realiza unao varias acciones específicas. Puede ser definido con la palabra reservada "def"
Método: Función predesarrollada dentro del propio lenguaje de programación, que se asocia a un objeto específico y que se llama directamente en ese objeto.
"""


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