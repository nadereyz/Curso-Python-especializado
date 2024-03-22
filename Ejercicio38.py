tuplas_numeros = (
    (1, 2, 3, 4, 5)
)

conjunto_numeros = (
    (1, 2, 3, 4, 5)
)

conjunto_numeros.add(6)


conjunto_numeros.remove(3)

copia_conjunto = {4, 5, 6, 7, 8}

unir_conjuntos = conjunto_numeros.union(copia_conjunto)


interseccion_conjuntos = conjunto_numeros.intersection(copia_conjunto)


diferencia_conjuntos = conjunto_numeros.difference(copia_conjunto)


diferencia_simetrica_conjuntos = conjunto_numeros.symmetric_difference(copia_conjunto)


# Convierte la tupla en un conjunto
tupla_conjunto = set(tuplas_numeros)

tupla_conjunto.add(6)
tupla_conjunto.remove(3)
union_tupla_conjunto = tupla_conjunto.union(copia_conjunto)
interseccion_tupla_conjunto = tupla_conjunto.intersection(copia_conjunto)
diferencia_tupla_conjunto = tupla_conjunto.difference(copia_conjunto)
diferencia_simetrica_tupla_conjunto = tupla_conjunto.symmetric_difference(copia_conjunto)
