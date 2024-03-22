
""" ¿Qué debo tener en cuenta al definir las claves de mis diccionarios?

· Naming: Es recomendable utilizar nombres descriptivos y significativos para las claves, de modo que reflejen el tipo de datos que representan. Por ejemplo, en un diccionario que almacena información de una persona, las claves podrían ser 'nombre', 'apellido', 'edad', etc.

· Duplicados: Las claves en un diccionario deben ser únicas. Si se intenta agregar una clave que ya existe, el valor asociado con esa clave se actualizará con el nuevo valor. Por lo tanto, es importante asegurarse de que las claves sean únicas para evitar la pérdida de datos.

· Inmutabilidad (de las claves de un diccionario, no de los valores, los valores son mutables): Las claves de un diccionario deben ser objetos inmutables, lo que significa que no pueden cambiar de valor después de ser creadas. Esto generalmente limita las claves a tipos de datos inmutables como cadenas, enteros y tuplas. Las listas y otros diccionarios no pueden usarse como claves porque son mutables.

· Hashable: Para que un objeto pueda ser utilizado como clave en un diccionario, debe ser "hashable", es decir, debe poder generar un valor hash único que se utilizará para buscar y almacenar la clave en la tabla hash interna del diccionario. 

· Caracteres especiales: Las claves de un diccionario pueden incluir caracteres especiales como guiones bajos (_), guiones (-), números, letras y otros caracteres especiales, siempre que cumplan con las reglas de nomenclatura de Python y sean "hashable"."""

#Acceder a diccionarios anidados: Para acceder a los elementos de los diccionarios anidados al diccionario principal, simplemente utilizamos la notación de corchetes [ ] y el nombre de la clave correspondiente. Podemos acceder a cualquier nivel de anidación dentro del diccionario principal utilizando la notación de corchetes y las claves adecuadas.
diccionario_base = {
    "diccionario anidado" : {
        "clave1" : 'valor x',
        "clave2" : 'valor x',
        "clave3" : 'valor x',
        "clave4" : 'valor x',
    }
}

contacto = {
    'nombre': 'Juan',
    'apellido': 'Gómez',
    'edad': 30,
    'telefono': '123456789',
    'nombre': 'Pepe', #En claves modificadas prevalece el valor que sea dispuesto en último lugar
    'email': 'juan@example.com',
    'direccion': {
        'calle': 'Calle Principal',
        'numero': '123',
        'ciudad': 'Ciudad Principal',
        'codigo_postal': '12345',
        'pais': 'País Principal',
        'familia': {
            'madre':'Doña Maria',
            'hermano':'Luis',
            'padre': 'Segisferio'
            },
        },
    'redes_sociales': {
        'twitter': '@juan_gomez',
        'facebook': 'JuanGomez',
        'instagram': 'juangomezofficial'
    },
    'intereses': {
        'principal': 'volar',
        'secundario': 'Programar en Python',
        'otros_intereses': ['viajes', 'lectura', 'deporte']
    }
}

# Acceder al número de teléfono
print("Teléfono (clave de primer nivel):", contacto['telefono'])

# Acceder al número de casa de la dirección
print("Número de casa (clave de segundo nivel):", contacto['direccion']['numero'])
print( "El código postal es (clave de segundo nivel):", contacto['direccion']['codigo_postal'])
print("La ciudad principal (clave de segundo nivel):", contacto['direccion']['ciudad'])
print("El nombre de la madre es (clave de tercer nivel):", contacto['direccion']['familia']['madre'])

# Acceder al nombre de usuario de Twitter
print("Usuario de Twitter:", contacto['redes_sociales']['twitter'])

# Acceder al primer interés
print("Primer interés dentro de otros intereses:", contacto['intereses']['otros_intereses'][0])




#--------------------MÉTODOS DICCIONARIOS------------------

#Método clear(): Elimina todos los elementos del diccionario, dejándolo vacío.
diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario.clear()
print("Mi diccionario con todos los elementos eliminados es:", diccionario)  # Salida: {} --> diccionario vacio, ya que los conjuntos vacios se representan 'set()'

#Método copy(): Devuelve una copia superficial del diccionario.
diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario_copia = diccionario.copy()
print("diccionario copia:", diccionario_copia)  # Salida: {'a': 1, 'b': 2, 'c': 3}

#Método get(): devuelve el valor de una clave especificada. Si la clave no existe, devuelve un valor predeterminado (None si no se especifica otro valor)
valor = diccionario.get('a')
print(valor)  # Salida: 1

#Método items() --> ELEMENTOS COMPLETOS (clave + valor): Devuelve todos los pares clave-valor en el diccionario como tuplas.
pares = diccionario.items()
print(pares)  # Salida: dict_items([('a', 1), ('b', 2), ('c', 3)])

#Método keys(): Devuelve una lista de todas las claves en el diccionario.
claves = diccionario.keys()
print(claves)  # Salida: dict_keys(['a', 'b', 'c'])

#Método values(): Devuelve todos los valores en el diccionario.
valores = diccionario.values()
print(valores)  # Output: dict_values([1, 2, 3])

#Ejemplo con el diccionario contacto inicializado y definido anteriormente
elementos_contacto = contacto.items()
claves_contacto = contacto.keys()
valores_contacto = contacto.values()

print("Los elementos del diccionario contactos son\n: ", elementos_contacto)
print("Las claves del diccionario contactos son\n: ", claves_contacto)
print("Los valores del diccionario contactos son\n: ", valores_contacto)
