# 1. Creación de conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 2. Unión de conjuntos
union = set1.union(set2)

# 3. Intersección de conjuntos
interseccion = set1.intersection(set2)

# 4. Diferencia de conjuntos (set1 - set2)
diferencia = set1.difference(set2)

# 5. Diferencia simétrica de conjuntos
diferencia_simetrica = set1.symmetric_difference(set2)

# 6. Verificar si set1 es un subconjunto de set2
es_subconjunto = set1.issubset(set2)

# 7. Verificar si set1 es un superconjunto de set2
es_superconjunto = set1.issuperset(set2)

# 8. Mostrar resultados
print("Unión de conjuntos:", union)
print("Intersección de conjuntos:", interseccion)
print("Diferencia de conjuntos (set1 - set2):", diferencia)
print("Diferencia simétrica de conjuntos:", diferencia_simetrica)
print("¿set1 es un subconjunto de set2?:", es_subconjunto)
print("¿set1 es un superconjunto de set2?:", es_superconjunto)



