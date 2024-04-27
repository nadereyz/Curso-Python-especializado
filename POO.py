# --------- PROGRAMACIÓN ORIENTADA A OBJETOS (POO)--------------
"""from archivo import clase"""

"""
Surge en los años '70. Utiliza las clases para organizar el código de tal forma que nos permita agrupar conjuntos de variables y funciones para posteriormente utilizarlas.
Un objeto es una entidad que combina datos (llamados atributos) y funciones especifícas de estas clases (llamados métodos)
Para definir clases, utilizaré el CamelCase en caso de el naming de mis clases incluyan dos o más palabras. Además está aceptado y normalizado el uso de mayúsculas para definir las clases. Debemos tener en cuenta que Python es keysensitive, es decir: class Coche & class coche--> No es lo mismo
Los nombres de métodos y atributos deben usar minúsculas con palabras separadas por guiones bajos.

CARACTERÍSTICAS:

· Reutilización de código: Puedes reutilizar clases ya definidas en otros programas, lo que ahorra tiempo y esfuerzo.
· Organización: La POO organiza el código de una manera más estructurada y fácil de entender, especialmente en proyectos grandes.
· Abstracción: Permite pensar en términos de objetos del mundo real, lo que facilita el diseño y la comprensión del código.
Mantenimiento: Los cambios en una parte del código pueden hacerse más fácilmente sin afectar otras partes, siempre y cuando se mantenga la interfaz de los objetos.
· Encapsulamiento: Permite ocultar detalles internos de los objetos, protegiendo así la integridad del sistema y facilitando la modificación de su comportamiento sin afectar a otras partes del programa.
"""
""" class Coche:
    def acelerar(self): #El parámetro self es una referencia a la propia instancia de la clase. Es necesario incluirlo como primer parámetro en TODOS los métodos de instancias de una clase de Python
       print("El coche está acelerando")
       
    def frenar(self):
        print("El coche está frenando")
        
        
mi_coche = Coche()

mi_coche.frenar()


class Cliente:
    
    def __init__(self, codigo_postal, direccion): #El constructor __init__ es un método especial que se utiliza para proporcionar valores iniciales a los atributos de mi objeto. 
        self.codigo_postal = codigo_postal
        self.direccion = direccion 
    
    def establecer_nombre(self, nombre): #Este método nos permite establecer un nombre de mi cliente. Coge un parámetro 'nombre' y lo asigna al atributo nombre del objeto Cliente
        self.nombre = nombre
        
    def obtener_nombre(self):
        return self.nombre
    
    def establecer_edad(self, edad: int):
        self.edad = edad
    
    def obtener_edad(self):
        return self.edad

#Creo una instancia (copia) de mi clase y asigno valores a los atributos de mi instancia      
cliente_uno = Cliente()
cliente_uno.direccion = "Avenida de los Rosales, 357 AtB"

#Creo más instancias de mi clase 
cliente_dos = Cliente()
cliente_tres = Cliente()
#Asigno un valor a la variable nombre_uno
nombre_uno = str(input("Establece un nombre"))
#Asigno un valor a la variable edad_uno
edad_uno = int(input("Dime tu edad"))
#Establezco un valor al atributo nombre de mi clase Cliente
cliente_dos.establecer_nombre("Hachiko")
#Asigno al atributo nombre de mi objeto cliente_uno el valor almacenado en la variable nombre_uno
cliente_uno.establecer_nombre(nombre_uno)
#Asigno al atributo edad de mi objeto cliente_uno el valor 40
cliente_uno.establecer_edad(40)
#Imprimo el nombre de mi cliente_uno utilizando el método obtener_nombre de mi clase Cliente
print("Nombre de mi cliente uno es:", cliente_uno.obtener_nombre()) """
        

""" 
· Clases: Bloques de construcción que me permiten definir plantillas. Estas plantillas van a definir las propiedades y comportamientos de un objeto. Es como un plano o un molde que define las características y comportamientos que tendrán los objetos que se crearán a partir de ella.  

· Objeto: Los objetos son instancias de las clases. Cada objeto creado a partir de una clase tiene su propia copia de atributos y de métodos, pudiendo llamar a esos métodos. Por ejemplo, si creamos el objeto cliente_uno a partir de la clase Cliente, cliente_uno tendrá sus propios valores para nombre y edad, y serán independientes de otros objetos que creemos de la misma clase, por ejemplo cliente_dos, cliente_tres.....

· Atributo: Los atributos son variables asociadas a una clase que representan sus carácterísticas (en el ejemplo de la clase cliente: nombre, edad). Pueden ser datos simples como números o cadenas, o incluso otros objetos como ya veremos.
 
· Métodos: Los métodos son funciones asociadas a una clase que definen su comportamiento. Pueden acceder y modificar los atributos del objeto al que pertenecen. 

"""
""" 
class CocheEjemplo:
    #PRIMER BLOQUE: ATRIBUTOS ESTÁTICOS
    material = "plástico" #Característica/atributo estático
    
    #SEGUNDO BLOQUE: ATRIBUTOS DINÁMICOS
    #Método especial constructor
    def __init__(self, color, puertas, llantas): #Atributos que serán definidos en cada una de las instancias de la clase
        self.color = color
        self.puertas = puertas
        self.llantas = llantas
   
    
    #TERCER BLOQUE: MÉTODOS
    #Método de instancia
    def arrancar(self):
        print(f"El coche {self.color} está arrancando")
    
coche_uno = CocheEjemplo("rojo", "3 puertas", "5 llantas")
coche_dos = CocheEjemplo("amarillo", "5 puertas", "4 llantas")


coche_uno.arrancar()

Caracteríscas del coche 1 son:
· Rojo
· 3 puertas
· 5 llantas
· Material plástico
Caracteríscas del coche 2 son:
· Amarillo
· 5 puertas
· 4 llantas
· Material plástico


print(coche_dos.material)

class personas:
    def __init__(self, nombre1, edad1, color_de_piel1):
        self.nombre = nombre1
        self.edad = edad1
        self.color_de_piel = color_de_piel1

#Solicito al usuario la entrada de datos y los almaceno en variables
nombre_uno = str(input("¿Cuál es tu nombre?\n"))
edad_uno = int(input("¿Cuántos años tienes?\n"))
color_piel_uno = str(input("¿De qué raza eres?\n"))
#Creo un objeto de la clase personas y le añado como atributos los valores almacenados en las variables en el paso anterior
persona1 = personas(nombre_uno, edad_uno, color_piel_uno)


print("Tu nombre es ", persona1.nombre," y tienes", persona1.edad, "años.")
print("Tú eres una persona con piel de color ", persona1.color_de_piel)



#EJERCICIO TRABAJADOR RESUELTO CON MÉTODOS DE CLASE
class Trabajador:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        
    @classmethod 
    #Este método se asocia con la clase y no con los objetos  
    #Defino una función para que el usuario puedad agregar un nuevo trabajador
    def agregar_trabajador(cls, lista_trabajadores):
        print("Introduce los datos del nuevo trabajador:\n")
        nombre = str(input("Introduce el nombre del nuevo trabajador:\n"))
        edad = int(input("Introduce la edad del nuevo trabajador:\n"))
        salario = int(input("Introduce el salario del nuevo trabajador:\n"))
        trabajador_nuevo = cls(nombre, edad, salario)
        lista_trabajadores.append(trabajador_nuevo)
    
    @classmethod 
    def mostrar_trabajador(cls, lista_trabajadores):
        print("Lista de trabajadores:\n")
        for i, trabajador in enumerate(lista_trabajadores, start=1):
            print(f"Trabajador {i}:")
            print(f"Nombre: {trabajador.nombre}")
            print(f"Edad: {trabajador.edad}")
            print(f"Salario: {trabajador.salario}")
            print()
            

trabajadores = []

while True:
    print("Selecciona una de las siguientes opciones:\n")
    print("1 - Agregar trabajador\n")
    print("2 - Mostrar trabajadores\n")
    print("3 - Salir\n")
    
    opcion = int(input("Escribe el número vinculado a la opción que deseas: \n"))
    
    if opcion == 1:
        Trabajador.agregar_trabajador(trabajadores)
    elif opcion == 2:
        Trabajador.mostrar_trabajador(trabajadores)
    elif opcion == 3:
        break
    
"""
#EJERCICIO TRABAJADOR RESUELTO CON MÉTODOS DE INSTANCIA
class TrabajadorDos:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def agregar_trabajador(self, lista_trabajadores):
        print("Introduce los datos del nuevo trabajador:\n")
        nombre = str(input("Introduce el nombre del nuevo trabajador:\n"))
        edad = int(input("Introduce la edad del nuevo trabajador:\n"))
        salario = int(input("Introduce el salario del nuevo trabajador:\n"))
        trabajador_nuevo = TrabajadorDos(nombre, edad, salario)
        lista_trabajadores.append(trabajador_nuevo)
        print("Trabajador agregado corectamente")
     
    def mostrar_trabajador(self, lista_trabajadores):
        print("Lista de trabajadores:\n")
        for i, trabajador in enumerate(lista_trabajadores, start=1):
            print(f"Trabajador {i}:")
            print(f"Nombre: {trabajador.nombre}")
            print(f"Edad: {trabajador.edad}")
            print(f"Salario: {trabajador.salario}")
            print()

trabajadores = []

#Necesito crear una instancia de mi clase para poder trabajar con sus métodos, ya que son métodos de instancia y no son métodos de clase
empresa = TrabajadorDos("", 0, 0)

while True:
    print("Selecciona una de las siguientes opciones:\n")
    print("1 - Agregar trabajador\n")
    print("2 - Mostrar trabajadores\n")
    print("3 - Salir\n")
    
    opcion = int(input("Escribe el número vinculado a la opción que deseas: \n"))
    
    if opcion == 1:
        empresa.agregar_trabajador(trabajadores)
    elif opcion == 2:
        empresa.mostrar_trabajador(trabajadores)
    elif opcion == 3:
        break
    
"""

----- MÉTODO DE CLASE -----
--> Actúa sobre la propia clase, en vez de actuar sonbre las instancia
--> Pueden ser llamados directamente desde la clase sin necesidad de crear una instancia.
--> Se definen utilizando el decorador @classmethod y automáticamente va a tomar como primer parámetro 'cls'
--> Pueden ser llamados directamente desde la clase, sin necesidad de crear una instancia
class MiClase:
    @classmethod
    def mi_metodo_de_clase(cls, parámetro1, parametro2....)
    --> Utilizo cls para acceder a la clase.
    --> Realizar operaciones vinculadas con la clase.
    
----- MÉTODO DE INSTANCIA -----
--> Actúa siempre sobre las instancias individuales de una clase
--> Son utilizados para realizar operaciones específicas para cada instancia de la clase
--> Se definen dentro de la clase sin utilizar ningún decorador y automáticamente utiliza como primer parámetro 'self'. 
--> Podré acceder a los atributos de la instancia utilizando 'self'
"""
#EJEMPLO MÉTODO DE INSTANCIA: Actúan sobre las instancias individuales
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre}, y tengo {self.edad} años"
    
persona_uno = Persona("Juan", 30)
persona_dos = Persona("Pepe", 24)

print(persona_uno.saludar())
print(persona_dos.saludar())

#EJEMPLO MÉTODO DE CLASE
class Familia:
    hijos = 10
    
    def __init__(self, manos):
        self.manos = manos
        
    @classmethod
    def definir_nuevo_numero_hijos(cls, nuevo_valor): #Defino un método de clase para cambiar el valor de un atributo estáticos
        cls.hijos = nuevo_valor
    
    @classmethod
    def calcular_manos(cls, manos):
        return cls.hijos * manos

#Llamar al método de clase para definir pi sin necesidad de crear previamente una instancia
nuevo_valor = float(input("Introduce un nuevo número de hijos"))
Familia.definir_nuevo_numero_hijos(nuevo_valor)  
#Llamar al método de clase para calcular el área del círculo sin necesidad de crear previamente una instancia
print(Familia.calcular_manos(3))  

