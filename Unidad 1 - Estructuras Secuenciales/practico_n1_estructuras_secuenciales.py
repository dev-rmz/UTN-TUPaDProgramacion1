import math
#Práctico 1: Estructuras secuenciales
#Actividades

'''
1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
'''

print("Hola Mundo!")

'''
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe 
imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
'''

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre} !") 


'''
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario
 ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas
   print(f…) para realizar la impresión por pantalla.
'''

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

'''
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
'''

radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")

'''
5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
'''

segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60
print(f"Horas:minutos:segundos: {horas}:{minutos}:{segundos}")

'''
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
'''

numero = int(input("Ingrese un numero: "))
for i in range(0,11):
    print(f"{numero} * {i} = {numero * i}")

'''
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
'''

primerNumero = int(input("Ingrese primer numero distinto de 0: "))
segundoNumero = int(input("Ingrese segundo numero distinto de 0: "))
print(f"Suma: {primerNumero + segundoNumero}")
print(f"Division: {primerNumero // segundoNumero}")
print(f"Multiplicacion: {primerNumero * segundoNumero}")
print(f"Resta: {primerNumero - segundoNumero}")

'''
8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula 
del siguiente modo:   IMC: (peso en kg)/(altura en m^2)
'''

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}") #imc:.2f muentra en dos decimales

'''
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente 
equivalencia:     Temperatura en Fahrenheit = ((9/5) * Temperatura en celsius) + 32

'''

tempCelsius = float(input("Ingrese temperatura en ° Celsius: "))
tempFahrenheit = ((9/5) * tempCelsius) + 32
print(f"Temperatura en Fahrenheit: {tempFahrenheit}")

'''
10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
'''

num1 = int(input("Ingrese primer numero entero positivo: "))
num2 = int(input("Ingrese segundo numero entero positivo: "))
num3 = int(input("Ingrese tercer numero entero positivo: "))
promedio = (num1 + num2 + num3) / 3
print(f"Promedio: {promedio}")