class Persona:
    def __init__(self, nombre:str, edad:int, genero:str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
#Guarda los datos atraves de open en el sitio especificado
def guardar_datos(gestor_persona, ruta):
    with open(ruta, 'w') as f:
        for persona in gestor_persona:
            f.write(f"Nombre: {persona.nombre}, Edad: {persona.edad}, Genero: {persona.genero}\n")


def main():
    gestor_persona = []
    ruta_predeterminada = r"C:\Users\jfely\Documents\Test\datos.txt"
    while True:
        print("Bienvenido, empezamos a trabajar:")
        print("1- Listado")
        print("2- Crea una persona nueva")
        print("3- Modifica datos")
        print("4- Guardar datos")
        print("5- Cerrar")
        opcion = input("Elige una opcion\n")
    #Creamos las opciones, cada una tendra su codigo especifio
        #Imprime la lista de las personas registradas con sus datos personales    
        if opcion == '1':
            print("\nLista de personas:")
            for i, persona in enumerate(gestor_persona):
                print(f"Persona {i+1} - Nombre: {persona.nombre}, Edad: {persona.edad}, Genero: {persona.genero}")
                
        #Crea el registro de una nueva persona y la agrega a la class 'Persona'
        elif opcion == '2':
            while True:
                nombre = input("Introduce el nombre:\n").capitalize()
                if nombre.isdigit():
                    print("Has introducido números, por favor introduce un nombre válido.")
                    continue
                
                    
                while True:
                    try:
                        edad = int(input("Introduce la edad:\n"))
                        break
                    except ValueError:
                        print("Tienes que poner la edad con números")

                #Registra por ultimo la variable 'genero' si eliges algo que no sean esas dos opciones crea un break, futuro cambiar a bucle while
                genero = str(input("Introduce el genero 'm' o 'f':\n"))
                while genero.lower() not in ["m", "f"]:
                    print("No has elegido bien, tus opciones son:\n 'm' o 'f'")
                    genero = str(input("Introduce el genero 'm' o 'f':\n"))
                #
                persona = Persona(nombre, edad, genero)
                gestor_persona.append(persona)
                #Pregunta si añadimos otro usuario o volvemos a la lista de opciones
                otro_usuario = input("¿Añadimos mas datos?? (s/n): ")  
                if otro_usuario.lower() == "s":
                    opcion = "2"
                elif otro_usuario.lower() == "n":
                    break
        #Crea un inicio de moficacion de los datos de una 'persona' dentro de 'class Persona'
        elif opcion == '3':
            print("\nModificar datos de una persona:")
            for i, persona in enumerate(gestor_persona):
                print(f"Persona {i+1} - Nombre: {persona.nombre}, Edad: {persona.edad}, Genero: {persona.genero}")
            indice = int(input("Elige el número de la persona a modificar: ")) - 1
            if indice < 0 or indice >= len(gestor_persona):
                print("Número inválido. Inténtalo de nuevo.")
            else:
                nombre = str(input("Introduce el nuevo nombre:\n").capitalize())
                if not isinstance(nombre, str):
                    print("Tienes que introducir un nombre")
                else:
                    edad = int(input("Introduce la nueva edad:\n"))
                if not isinstance(edad, int):
                    print("Tienes que poner la edad con números")
                else:
                    genero = str(input("Introduce el nuevo genero 'm' o 'f':\n"))
                    if genero.lower() not in ["m", "f"]:
                        print("Elige entre 'm' o 'f'")
                    else:
                        #Verifica los datos
                        gestor_persona[indice].nombre = nombre
                        gestor_persona[indice].edad = edad
                        gestor_persona[indice].genero = genero
                        print("Datos modificados con éxito.")
        elif opcion == '4':
            guardar = input("¿Deseas guardar en la ruta predeterminada? (s/n): ")
            if guardar.lower() == 's':
                guardar_datos(gestor_persona, ruta_predeterminada)
                print("Datos guardados en la ruta predeterminada.")
            else:
                ruta_personalizada = input("Introduce la ruta completa para guardar los datos: ")
                guardar_datos(gestor_persona, ruta_personalizada)
                print("Datos guardados en la ruta especificada.")
        elif opcion == '5':
            print("Cerrando el programa.")
            break
    print("\n😊", "-"*13, "Adios", "-"*13, "😊")

main()