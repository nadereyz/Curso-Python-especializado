
# BLOQUE NÚMERO 2
Programa de Información Personal # aqui tiene que ser un comentario o un print.
print( "¡Bienvenido al Programa de Información Personal!\n" )

# Mensaje personalizado usando .format()
mensaje_format = "¡Hola, {}, ! Bienvenido a {}.".format(nombre, ciudad); # primero hay que crear los 2 variables nombre y ciudad, 
                                                                        # el tema de format no se usa [], se usa parentesis (), y despues de "" hay que concatenar con .format 
# Entrada de datos
nombre = input ("Introduce tu nombre: ") #poner espacio + añadir ""
edad = input ("Introduce tu edad: ") # poner espacio
ciudad = input ("Introduce tu ciudad de residencia: ") # poner espacio + las comillas tienen que ser iguales " = "  o  ' = '



# Mensaje personalizado usando f-string
mensaje_fstring = F"Esperamos que disfrutes tu estadía. Tienes {edad:x.2h} años de sabiduría."     # tiene que ser edad:.2f

# Mostrar resultados
print(mensaje_format x 2)
print(mensaje_fstring) # hay que declarar bien la variable
