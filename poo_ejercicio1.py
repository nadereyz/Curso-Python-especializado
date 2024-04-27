class Trabajador:
    lista_trabajadores = []

    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    @classmethod
    def agregar_trabajador(cls):
        print("\nAgregar datos del nuevo trabajador: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        salario = float(input("Salario: "))
        nuevo_trabajador = cls(nombre, edad, salario)  # cls se usa para referenciar a la clase Trabajador
        cls.lista_trabajadores.append(nuevo_trabajador)
        print("Datos añadidos correctamente.")

    @classmethod
    def mostrar_trabajadores(cls):
        if not cls.lista_trabajadores:
            print("No hay trabajadores para mostrar.")
            return
        print("\nLista de trabajadores: ")
        for i, trabajador in enumerate(cls.lista_trabajadores, start=1):
            print(f"Trabajador {i}:")
            print(f"Nombre: {trabajador.nombre}")
            print(f"Edad: {trabajador.edad}")
            print(f"Salario: {trabajador.salario}\n")

    @classmethod
    def actualizar_trabajador(cls):
        nombre = input("Pon el nombre para que puedas modificar: ")
        for trabajador in cls.lista_trabajadores:
            if trabajador.nombre == nombre:
                trabajador.edad = int(input("Nueva edad: "))
                trabajador.salario = float(input("Nuevo salario: "))
                print("Actualizando....")
                print("Trabajador actualizado correctamente.")
                return
        print("Trabajador no encontrado.")

    @classmethod
    def borrar_trabajador(cls):
        nombre = input("Pon el nombre del trabajador a borrar: ")
        for i, trabajador in enumerate(cls.lista_trabajadores):
            if trabajador.nombre == nombre:
                del cls.lista_trabajadores[i]
                print("Trabajador borrado correctamente.")
                return
        print("Trabajador no encontrado.")


while True:
    print("\nBienvenido")
    print("1-> Agregar")
    print("2-> Actualizar")
    print("3-> Borrar")
    print("4-> Mostrar")
    print("5-> Salir")

    opcion = input("Escoje la opcion: ")

    if opcion == '1':
        Trabajador.agregar_trabajador()
        input("Presiona Enter para continuar...")
    elif opcion == '2':
        Trabajador.actualizar_trabajador()
        input("Presiona Enter para continuar...")
    elif opcion == '3':
        Trabajador.borrar_trabajador()
        input("Presiona Enter para continuar...")
    elif opcion == '4':
        Trabajador.mostrar_trabajadores()
        input("Presiona Enter para continuar...")
    elif opcion == '5':
        print("Saliendo...")
        break
    else:
        print("No es valido, por favor vuelve a poner entre 1 a 5.")
