#Práctico 2: Funciones en Python
#Actividades:

'''
1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
'''

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


'''
2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el 
nombre al usuario.
'''

def saludar_usuario(nombre):
    saludo = "Hola " + nombre + "!"
    return saludo

nombre_ingresado = input("Ingrese su nombre: ")
mensaje = saludar_usuario(nombre_ingresado)
print(mensaje)

'''
3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], 
tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

'''
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
'''
import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)

'''
5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
 Solicitar al usuario los segundos y mostrar el resultado usando esta función.
'''

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos: "))

resultado = segundos_a_horas(segundos)
print("Equivale a", resultado, "horas.")

'''
6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10.
 Pedir al usuario el número y llamar a la función.
'''

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

'''
7. Crear una función llamada operaciones_basicas(a, b) que recibados números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, 
multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
'''
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)

print("Resultados:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

'''
8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).
 Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
'''

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso, altura)

print(f"Su índice de masa corporal (IMC) es: {resultado:}")

'''
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
'''

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {resultado:}°F")

'''
10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función.
'''
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

resultado = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {resultado}")


