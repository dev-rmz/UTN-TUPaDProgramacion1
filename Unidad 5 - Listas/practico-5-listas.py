#Práctico 5: Listas
#Actividades

'''
1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
'''
notas = [7, 8, 5, 9, 10, 6, 4, 7, 8, 9]
print("Notas de los estudiantes:")

for i in range(len(notas)):
    print(f"Estudiante {i+1}: {notas[i]}")

suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"Promedio de notas: {promedio}")

nota_max = notas[0]
nota_min = notas[0]

for nota in notas:
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota

print(f"Nota mas alta: {nota_max}")
print(f"Nota mas baja: {nota_min}")

'''
2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
'''

productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

print("Lista de productos ordenada alfabéticamente:")
productos_ordenados = sorted(productos)
for p in productos_ordenados:
    print(p)

elim = input("Ingrese el nombre del producto que desea eliminar: ")

if elim in productos:
    productos.remove(elim)
    print("Producto eliminado correctamente.")
else:
    print("El producto no se encuentra en la lista.")

print("Lista actualizada:")
for p in productos:
    print(p)

'''
3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista.
'''
import random

numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

print("Lista generada:")
for n in numeros:
    print(n, end=" ")

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\n\nNúmeros pares:")
for p in pares:
    print(p, end=" ")
print(f"\nCantidad de pares: {len(pares)}")

print("\nNúmeros impares:")
for imp in impares:
    print(imp, end=" ")
print(f"\nCantidad de impares: {len(impares)}")

'''
4) Dada una lista con valores repetidos: datos= [1, 3, 5, 3, 7, 1, 9, 5, 3]
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.
'''
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sin_repetidos = []

for num in datos:
    if num not in sin_repetidos:
        sin_repetidos.append(num)

print("Lista original:")
for d in datos:
    print(d, end=" ")

print("\n\nLista sin repetidos:")
for d in sin_repetidos:
    print(d, end=" ")

'''
5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.
'''

estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena", "Facundo", "Gabriela", "Hernán"]
print("Lista inicial de estudiantes:")
for e in estudiantes:
    print(e)

opcion = input("\n¿Desea agregar o eliminar un estudiante? (escriba 'agregar' o 'eliminar'): ").lower()

if opcion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\nSe agregó a {nuevo} a la lista.")

elif opcion == "eliminar":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
        print(f"\nSe eliminó a {borrar} de la lista.")
    else:
        print("\nEse estudiante no está en la lista.")

else:
    print("\nOpción no válida, no se realizaron cambios.")

print("\nLista final de estudiantes:")
for e in estudiantes:
    print(e)

'''
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
'''

numeros = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:")
for n in numeros:
    print(n, end=" ")


ultimo = numeros[-1]
for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1]
numeros[0] = ultimo

print("\n\nLista rotada a la derecha:")
for n in numeros:
    print(n, end=" ")

'''
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.
'''
temperaturas = [
    [12, 20],  
    [14, 22],  
    [10, 18],  
    [13, 25],  
    [11, 21],  
    [15, 28],  
    [9,  19]   
]

suma_min = 0
suma_max = 0

for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"Promedio de mínimas: {promedio_min:.2f}°C")
print(f"Promedio de máximas: {promedio_max:.2f}°C")

mayor_amplitud = 0
dia_mayor = 0

for i in range(len(temperaturas)):
    min_temp = temperaturas[i][0]
    max_temp = temperaturas[i][1]
    amplitud = max_temp - min_temp

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1 

print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C y ocurrió el día {dia_mayor}.")

'''
8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.
'''
notas = [
    [7, 8, 6],  
    [5, 9, 7],  
    [6, 6, 8],  
    [9, 7, 10], 
    [8, 8, 9]   
]

print("Promedio de cada estudiante:")
for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    promedio = suma / len(notas[i])
    print(f"Estudiante {i+1}: {promedio:.2f}")

print("\nPromedio de cada materia:")
materias = len(notas[0])

for j in range(materias):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    promedio = suma / len(notas)
    print(f"Materia {j+1}: {promedio:.2f}")

'''
9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada.
'''
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

print("Tablero inicial:")
mostrar_tablero(tablero)

for turno in range(2):
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"

    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingrese la fila (0-2): "))
    col = int(input("Ingrese la columna (0-2): "))

    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("Casilla ocupada, pierde el turno.")

    mostrar_tablero(tablero)

'''
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.
'''
ventas = [
    [5, 3, 4, 2, 6, 1, 3],  
    [2, 4, 3, 5, 3, 2, 4],  
    [3, 5, 2, 4, 3, 5, 2],  
    [4, 2, 5, 3, 4, 3, 5]   
]

print("Total vendido por cada producto:")
for i in range(len(ventas)):
    total_producto = sum(ventas[i])
    print(f"Producto {i+1}: {total_producto}")


total_por_dia = []
for j in range(len(ventas[0])):  
    suma_dia = 0
    for i in range(len(ventas)):
        suma_dia += ventas[i][j]
    total_por_dia.append(suma_dia)

dia_mayor = total_por_dia.index(max(total_por_dia)) + 1  
print(f"\nEl día con mayores ventas totales fue el día {dia_mayor} con {max(total_por_dia)} unidades vendidas.")

total_por_producto = [sum(fila) for fila in ventas]
producto_mas_vendido = total_por_producto.index(max(total_por_producto)) + 1
print(f"El producto más vendido en la semana fue el Producto {producto_mas_vendido} con {max(total_por_producto)} unidades.")
