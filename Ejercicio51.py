#EJEMPLO NACHO UTILIZANDO RETURN PARA VERIFICAR DIVISIBILIDAD

def verificar_divisibilidad(numero, divisores):
    resultados = []
    for divisor in divisores:
        if numero % divisor == 0:
            resultados.append(numero)
    if len(resultados) >= 1:
        return "Se han encontrado números divisibles" 
    else:
        return "No se han encontrado números divisibles"

numero = int(input("Introduce el numero a evaluar:\n"))
divisor1 = int(input("Introduce el primer divisor:\n"))
divisor2 = int(input("Introduce el segundo divisor:\n"))
divisores = [divisor1, divisor2]
resultado = verificar_divisibilidad(numero, divisores)
print(resultado)


#EJEMPLO NACHO NO UTILIZANDO RETURN PARA VERIFICAR DIVISIBILIDAD

def verificar_divisibilidad(numero, divisores):
    resultados = []
    for divisor in divisores:
        if numero % divisor == 0:
            resultados.append(numero)
    if len(resultados) >= 1:
        print("Se han encontrado números divisibles") 
    else:
        print("No se han encontrado números divisibles")

numero = int(input("Introduce el numero a evaluar:\n"))
divisor1 = int(input("Introduce el primer divisor:\n"))
divisor2 = int(input("Introduce el segundo divisor:\n"))
divisores = [divisor1, divisor2]
verificar_divisibilidad(numero, divisores)
