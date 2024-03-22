# definicion
# mutabilidad
# acceso_a_elementos
# tipos_de_datos
# orden
# duplicados
# metodos

diccionario_listas = {
    "definicion": ["Una lista es una colección ordenada y mutable de elementos"],
    "mutabilidad": ["Mutable: Pueden ser modificadas después de la creación"],
    "acceso_a_elementos": ["Por índice lista[0]"],
    "tipos_de_datos": ["Cadenas de texto, números (int & float), booleanos(no tiene mucho sentido), tuplas, conjuntos, diccionarios u otras listas"],
    "orden": ["Mantienen el orden de insercción"],
    "duplicados": ["Pueden contener elementos duplicados"],
    "metodos": ["append(), remove(), pop(), clear(), len(), index(), sort(), sorted()"],
}

diccionario_tuplas = {
    "definicion": ("Una tupla es una colección ordenada e inmutable de elementos"),
    "mutabilidad": ("Inmutables: No pueden ser modificadas después de la creacción"),
    "acceso_a_elementos": ("Por índice lista[0]"),
    "tipos_de_datos": ("Cadenas de texto, números, float, booleanos(no tiene mucho sentido), listas, conjuntos, diccionarios u otras tuplas"),
    "orden": ("Mantienen el orden de insercción"),
    "duplicados": ("Pueden contener elementos duplicados"),
    "metodos": ("append(), remove(), pop(), clear(), len(), index(), sort(), sorted()")
}

diccionario_conjuntos = {
    "definicion": {"Un conjunto es una colección desordenada y mutable de elementos únicos"},
    "mutabilidad": {"Mutable: Pueden ser modificadas después de la creación"},
    "acceso_a_elementos": {"No aplica (no tiene índices)"},
    "tipos_de_datos": {"Solo admiten elementos inmutables: cadenas de texto, números (int & float), tuplas o frozenset (conjuntos congelados)"},
    "orden": {"No mantienen el orden de insercción"},
    "duplicados": {"No pueden contener elementos duplicados"},
    "metodos": {"add(), len(), remove(), discard()…"}
}

diccionario_diccionarios = {
    "definicion": {"Un diccionario es una colección no ordenada de pares clave-valor"},
    "mutabilidad": {"Mutable: Pueden ser modificadas después de la creación"},
    "acceso_a_elementos": {"Clave (mi_diccionario['clave'])"},
    "tipos_de_datos": {"Cadenas de texto, números (int & float), tuplas, conjuntos, listas, e incluso otros diccionarios"},
    "orden": {"Mantienen el orden de insercción"},
    "duplicados": {"Sí pueden contener elementos duplicados (en claves) "},
    "metodos": {"clear(), copy(), items(), keys(), value()…"},

}
diccionarios = {
    "listas": diccionario_listas,
    "tuplas": diccionario_tuplas,
    "conjuntos": diccionario_conjuntos,
    "diccionarios": diccionario_diccionarios
}

tipo_coleccion = input("Escribe el nombre que quieres consultar --> (listas, tuplas, conjuntos, diccionarios): ")

coleccion_seleccionada = diccionarios.get(tipo_coleccion.lower())

print(f"Datos sobre {tipo_coleccion.capitalize()}:")
for clave, valor in coleccion_seleccionada.items():
    print(clave.capitalize() + ": " + str(valor))

