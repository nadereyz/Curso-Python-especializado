#Método pop(): Elimina un elemento por su clave y devuelve su valor. Si la clave no existe, lanza una excepción KeyError. ELIMINA + ALMACENA EL VALOR ELIMINADO
diccionario = {'a': 1, 'b': 2, 'c': 3}
valor_eliminado = diccionario.pop('a')
print("Valor eliminado: ", valor_eliminado, "\n Diccionario sin el valor 'a':", diccionario)


#Método popitem(): Elimina y devuelve el último par clave-valor insertado en el diccionario. La salida de este par será una tupla. Si el diccionario esta vacio, nos va arrojar un KeyError. NO ADMITE ARGUMENTOS
par_eliminado = diccionario.popitem()
print("\n Par eliminado: ", par_eliminado, "\n Diccionario sin los valores del par eliminado:", diccionario)
par_eliminado_dos = diccionario.popitem() #Aquí el diccionario se queda vacio
#par_eliminado_tres = diccionario.popitem() --> KeyError: 'popitem(): dictionary is empty
print("diccionario final:", diccionario)

#update(): Este método actualiza el dicionario con los elementos de otro diccionario. También puede actualizar el diccionario con pares CLAVE=VALOR proporcionados al métodos como argumentos (de palabra clave)
diccionario_uno = {'a': 1, 'b': 2}
diccionario_dos = {'c': 3, 'd': 4}
diccionario_uno.update(diccionario_dos)
print("\nDiccionario uno:", diccionario_uno, "\nDiccionario dos:", diccionario_dos)
diccionario_dos.update(diccionario_uno)
print("\nDiccionario uno, 2º parte:", diccionario_uno, "\nDiccionario dos. 2º parte:", diccionario_dos)

diccionario_uno.update(e=5, f=6)
print(diccionario_uno)

#Método setdefault(): Devuelve el valor de UNA clave que nosotros le especificamos pasándola como argumento. A diferencia del método get(), si la clave no existe, nos la va a insertar en el diccionario con el valor que le hemos especificado (Si no le especificamos un valor, la incluye con el valor None)
valor_setdefault = diccionario_uno.setdefault('g', 20)
valor_setdefault_dos = diccionario_uno.setdefault('h', 10)
valor_setdefault_tres = diccionario_uno.setdefault('i')
print(valor_setdefault)
print(valor_setdefault_dos)
print(valor_setdefault_tres)
print(diccionario_uno)


