#Ejemplo de iteración básica sobre un diccionario (solo una variable que empaqueta todo el elemento)
diccionario = {
    'perro': 'animal que ladra',
    'gato': 'animal que maulla',
    'pájaro': 'animal que pia'
    }

for elemento in diccionario: #Cuando estoy iterando sobre un diccionario, el bucle for de forma predeterminada itera sobre las claves. Es decir, cuando estamos iterando sobre un diccionario que contiene elementos (pares CLAVE - VALOR), la variable que definimos para identificar cada uno de esos elementos itera sobre la clave
    print(elemento, ":", diccionario[elemento])

#Iterando diccionarios con el método items(): Este método devuelve cada uno de los elementos del diccionario como una tupla. Por ende, cada tupla tiene dos objetos dentro (la clave y el valor)
for clave, valor in diccionario.items():
    print(clave, ":", valor)


#Iterando diccionarios con el método keys(): Este método en iteraciones sobre diccionarios nos va a devolver las claves del diccionario. 
for clave in diccionario.keys():
    print("La clave es: ", clave)
    print("El valor es:", diccionario[clave]) #Como no estoy iterando sobre los valores en el bucle for, para poder acceder a ellos necesitaré hacerlo a través de la clave

#Iterando diccionarios con el método values(): Este método en iteraciones sobre diccionarios nos va a devolver los valores del diccionario. 
for valor in diccionario.values():
    print("-El valor es: ", valor)

    ventas_enero = {
        "pantalla": 60,
        "teclado": 100,
        "raton": 80
    }

    producto_vendido = 0
    for producto, cantidad in ventas_enero.items():
        producto_vendido += cantidad
print("precio total con items: ", producto_vendido)



producto_vendido1 = 0
for cantidad1 in ventas_enero.values():
    producto_vendido1 += cantidad1
print("precio total con values: ", producto_vendido1)


producto_vendido2 = 0
for producto in ventas_enero.keys():
    producto_vendido2 += ventas_enero[producto]
print("precio total con keys: ", producto_vendido2)







