#OPERADORES DE IDENTIDAD--------------------

x = "Hola"
y = "Hola"
print(id(x), id(y)) # id indica la dirección del objeto en la memoria. El método id() nos devuelve la identidad de un objeto. Número entero que será único y constante durante toda la vida útil del objeto

lista_uno = [1,2,3]
lista_dos = [1,2,3]
tuplas_uno = (4,5)


#Diferencia entre operador is y operador ==
print(lista_uno == lista_dos) #Devuelve True porque evalúa los valores de la lista y en caso de que sean idénticos devolverá True
print(lista_uno is lista_dos) #Devuelve False porque la operación con is evalua si las dos variables apuntan al mismo objeto en la memoria
print(id(lista_uno), id(lista_dos))

x = 10
y = x
print(id(x), id(y))



""" Los operadores de identidad seran 
is: Devuelve True si ambas variables evaluadas apuntan al mismo objeto en la memoria
is not: Devuelve True si ambas variables NO apuntan al mismo objeto en la memoria
 """

#Operador is
a = 10
b = 10
print(a is b)   #True, porque ambos son referencias a el valor numerico 10 

#Operador is not
x = 10
y = 11
print("resultado de is not", x is not y) #True, porque las dos valiables apuntan a diferentes objetos en la memoria