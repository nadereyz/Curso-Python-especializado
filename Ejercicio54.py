class Estudiante:
    def __init__(self, nombre): #aqui se esta creando el objeto
        self.nombre = nombre #aqui se esta creando el nombre
        self.asistencia = 0 #aqui se esta creando la asistencia
        self.calificaciones = [] #aqui se esta creando una lista de calificacion

    def registrar_asistencia(self):
        self.asistencia += 1 #aqui se esta sumando 1 a la asistencia


    def agregar_calificacion(self, calificacion): #aqui se esta agregando la calificacion
        self.calificaciones.append(calificacion)

    def promedio_calificaciones(self): #aqui se esta calculando el promedio de las calificaciones
        total_calificaciones = sum(self.calificaciones) # aqui calcula la suma de tooooooda la calificaciones que van poniendo el usuario
        numero_de_calificaciones = len(self.calificaciones) # aqui con len esta calculando la cantidad de calificaciones que van poniendo el usuario
        promedio = total_calificaciones / numero_de_calificaciones # aqui se esta calculando el promedio de las calificaciones
        return promedio


print("***********" * 5)
nombre = input("Pon tu nombre: ")
estudiante = Estudiante(nombre) # aqui almaceno el nombre a la class
cantidad_dias_asistencia = int(input("Pon los días de asistencias: ")) # Pedir al usuario que ingrese el numero de dias de asistencia
estudiante.asistencia = cantidad_dias_asistencia # Asignar directamente el numero de dias de asistencia al atributo del estudiante

    
while True:
    entrada = str(input("Pon una o varias calificaciones | para salir tienes que escribir -> out: ")) # aqui es para poner las calificaciones que el usuario puso.

    if entrada.lower() == 'out': # si el usuario escribe out pues se sale del ciclo y con lower pues aunque ponga mayuscula pues se saldra igualmente.
        break
    estudiante.agregar_calificacion(float(entrada))
    
print("Resultados del Estudiante:")
print(f"Nombre: {estudiante.nombre}")
print(f"Días de asistencia: {estudiante.asistencia}")
print(f"Promedio de calificaciones: {estudiante.promedio_calificaciones():.2f}")

