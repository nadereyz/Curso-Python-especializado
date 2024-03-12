usuario1_nombre = "Alejandra"
usuario1_correo = "alesrin@kobalto.es"


usuario2_nombre = "Pepito"
usuario2_correo = "pepe@email.com"

usuario_actual = "alejandra"

#------------------------------------------

print("Verificación de Usuarios")
esta_registrado = usuario_actual in (usuario1_nombre, usuario2_nombre)
print(f"Usuario {usuario_actual} está registrado: {esta_registrado}")
#------------------------------------------
print("\nComprobación de Correo Electrónico")
mismo_correo = usuario1_correo is usuario2_correo
print(f"Ambos usuarios comparten el mismo correo electrónico: {mismo_correo}")
#------------------------------------------
print("\nIdentificación de Objetos")
objetos_diferentes = usuario1_nombre is not usuario2_nombre
print(f"Los objetos que representan a los usuarios son diferentes: {objetos_diferentes}")
