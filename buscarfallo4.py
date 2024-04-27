
#``````````````````````````````GRUPO 4``````````````````````````````````````````
# Clase para representar a una Persona y que te psicoanalice por tu edad y algun comodin que te preguntara y juntando datos te dara los consejos del dia

class Persona: #clas Persona: debería ser class Persona

#Lista_persona = ("Nombre", edad, self)#Lista_persona = "(Nombre", edad, self) parece ser un intento de crear una tupla, pero está mal formada y no se utiliza.

  def __init__(self, nombre, edad): #Constructor: El método constructor debe llamarse __init__ con doble subrayado al principio y al final.

    self._nombre = nombre  # Error de estilo: debería s er self._nombre para indicar que es un atributo protegido
    self._edad = edad  # Error de estilo: debería ser self._edad por la misma razón anterior
        
  def calcular_anio_nacimiento(self): #Error sangrado.
    anio_actual = 2024  # Año actual mejor sin Ñ
    return anio_actual - self._edad # Año actual mejor sin Ñ
        
  def __init__(self): # salida de datos de la funcion __init__
    edad = self.edad
    return f"Tu nombre: {self.nombre} y tu Edad es {edad} ¿es correcto?"

def print_info(self):
   print(f"Nombre: {self.nombre}, Edad: {self.edad}")   # Error de concepto: 'prints' no es una función, debería ser 'print'


# Función para calcular el máximo de dos números y comprobar con la edad del usuario saber si es mayor de edad???
def maximo(edad): #def maximo(edad, 18) tiene un error de sintaxis; debería ser def maximo(edad)
    if edad > 18: #faltan dos puntos.
        return True
    else:
        return False  # Error de sintaxis: falta ':' al final del 'if' y del 'else'
	
    if edad < 18: #El bucle while edad<18 (*:) está mal formado y no tiene sentido en el contexto dado cambiamos while por if
  	  print(f"Nombre: {self.nombre}, Edad: {self.edad}, Eres muy joven para conducir, te veo en unos años") #  prints(f"Nombre: {self.nombre}, Edad: {self.edad}")# debería ser print(f"Nombre: {self.nombre}, Edad: {self.edad}").

color_de_ojos = ["verde","azul", "marron","Negro" ] #Error de sintaxis: debería ser color_de_ojos  =["verde","azul", "marron","Negro" ]
    
consejos = {"hoy es tu dia", "tomatelo con calma", "ponte gafas de sol", "No le hagas mucho caso"} #tiene varios errores: ponte gafas de sol debería estar entre comillas y debería ser una lista, no un conjunto, si se desea mantener un orden.
    
def pregunta_clave(self): #En def pregunta_clave(self):, color_de_ojos no está definido dentro del método.
  ojos = input(f"Di que color de ojos tienes de esta lista (color_de_ojos)")
edad = float(input("Di que edad Tienes"))
anio_nacimiento = input(str{"En que año nacistes, es solo para comprobar :"}) #anio_nacimiento = str{"En que anyo nacistes, es solo para comprobar :)"} debería ser una llamada a input() y anyo debería ser año.Falta un operador de asignación en anio_nacimiento = str{"En que anyo nacistes, es solo para comprobar :)"}.

index1 = len(ojos)-1 #index1 = len(ojos)-1 y index2 = len(consejos)-1 no tienen sentido ya que ojos es una cadena de texto y consejos es un conjunto.
index2 = len(consejos)-1
while ojos == color_de_ojos[index1]:
        	for p in Persona
if p.edad < 18:
       	print(consejos[index2])
else:
        print(consejos[3])
return #Error de sintaxis: falta un 'return' en la función maximo.
       # Crear objeto de la clase Persona
persona = Persona("Alice", 30)  # Error de sintaxis: debería ser Persona, no person
                               # Error de concepto: _init_ es incorrecto, debería ser __init__     	
                               
persona.pregunta_clave() #persona.pregunta_clave() se ejecutará con errores debido a los problemas anteriores en la definición de pregunta_clave.


