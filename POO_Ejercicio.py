# ----------- 1º EJERCICIO --------


"""
class Tarea:
    def establecer_tipo(self, tipo):
        self.tipo = tipo

    def establecer_prioridad(self, prioridad):
        self.prioridad = prioridad


trabajo = Tarea()

tipo_trabajo = input("Pon primero tarea uno: ")
trabajo.establecer_tipo(tipo_trabajo)

prioridad_trabajo = input("que tipo de prioridad Alto - Medio - Bajo: ")
trabajo.establecer_prioridad(prioridad_trabajo)

print("Tarea 1:")
print(f"tipo: {trabajo.tipo}" )
print(f"Prioridad: {trabajo.prioridad}", )

trabajo2 = Tarea()

tipo_trabajo2 = input("\Pon primero tarea dos: ")
trabajo2.establecer_tipo(tipo_trabajo2)

prioridad_trabajo2 = input("que tipo de prioridad Alto - Medio - Bajo ")
trabajo2.establecer_prioridad(prioridad_trabajo2)



print("\nTarea 2:")
print(f"tipo: {trabajo2.tipo}")
print(f"Prioridad: {trabajo2.prioridad}") 

# ----------- 2º EJERCICIO --------
class Persona:
    def __init__(self, nombre, edad, color, profesion, estado_civil): #eso es metodo constructor
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.profesion = profesion
        self.estado_civil = estado_civil

    def hablar(self, mensaje): # self es el objeto que se esta creando. + Metodo de instancia
        return f"{self.nombre} dice: {mensaje}"

    def caminar(self, pasos):
        return f"{self.nombre} pasos en total es: {pasos} pasos."

    def mirar(self, objeto):
        return f"{self.nombre} esta mirando en {objeto}."

    def nacer(self):
        return f"{self.nombre} ha nacido."

    def morir(self, fecha):
        return f"{self.nombre} ha muerto lamentablemente. en el dia {fecha}"
    
    def mostrar_profesion(self):
        return f"{self.nombre} trabajaba como {self.profesion}."

persona1 = Persona("Pepito", 50, "moreno", "Clouder", "Casado") #Aqui pongo los datos de la persona.
print(persona1.hablar("hola soy Pepito."))
print(persona1.caminar(10))
print(persona1.mirar("el atardecer"))
print(persona1.nacer())
print(persona1.morir("1/11/2022")) #probando poniendo la fecha exacta de la muerte pero da error
                                    #La solucion es que en el metodo morir habia que poner otro parametro fecha.

print(persona1.mostrar_profesion()) #probando que sea uno especifico
print()
print(vars(persona1))

"""

class Trabajador:
    listasegundaparte_trabajadores = []

    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    

    #Defino una funcion para que el usuario pueda agregar un nuevo trabajador
    def agregar_trabajador(lista_trabajadores):
        print("\nAñade los datos del nuevo trabajador: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        salario = float(input("Salario: "))
        nuevo_trabajador = Trabajador(nombre, edad, salario)
        lista_trabajadores.append(nuevo_trabajador)
        print("Datos añadido ole.")
    
    def mostrar_trabajadores(lista_trabajadores):
        print("\nLista de trabajadores: ")
        for i, trabajador in enumerate(lista_trabajadores, start=1):
            print(f"Trabajador {i}:")
            print(f"Nombre: {trabajador.nombre}")
            print(f"Edad: {trabajador.edad}")
            print(f"Salario: {trabajador.salario}\n")

    def actualizar_trabajador(lista_trabajadores):
          nombre = str(input("Pon el nombre para que puedas modificar despues:"))
          for trabajador in lista_trabajadores:
              if trabajador.nombre == nombre:
                    print("Actualiza los datos: ")


while True:
    print("\nBienvenido")
    print("1- Agregar")
    print("2- Actualizar")
    print("3- Borrar")
    print("4- Mostrar")
    print("5- Salir")

    opcion = input("Selecciona la opcion: ")

    if opcion == '1':
        Trabajador.agregar_trabajador(listasegundaparte_trabajadores)
    elif opcion == '2':
        Trabajador.actualizar_trabajador()
    elif opcion == '3':
        Trabajador.borrar_trabajador()
    elif opcion == '4':
        Trabajador.mostrar_trabajadores()
        input("Presiona Enter para continuar...")
    elif opcion == '5':
        print("Saliendo...")
        break
    else:
        print("No es valido, por favor vuelve a poner entre 1 a 5.")
        
