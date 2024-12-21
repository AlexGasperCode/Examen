# Ejercicio número 1
# Imprimir del 1 al 10
for numero in range(1, 11):
    print(numero)
# Calcular la suma de los primeros números naturales
n = int(input("Introduce un número: "))
suma = n * (n + 1) // 2
print(f"La suma de los primeros {n} números naturales es: {suma}")


#  Ejercicio número 2
import math
n = int(input("Introduce un número: "))
if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = math.factorial(n)
    print(f"El factorial de {n} es: {factorial}")
# Tabla de multiplicar
numero = int(input("Introduce un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# Ejercicio número 3
# Solicitar al usuario la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C son equivalentes a {fahrenheit}°F.")
# Kilometros a millas
# Solicitar al usuario la distancia en kilómetros
kilometros = float(input("Introduce la distancia en kilómetros: "))
millas = kilometros * 0.621371
print(f"{kilometros} kilómetros son equivalentes a {millas:.2f} millas.")


#  Ejercicio número 4
# Definir el menú de comidas con sus precios
menu = {
    "1. Hornado": 6.50,
    "2. Mote con fritada": 6.00,
    "3. Caldo de 31": 4.20,
    "4. Humitas": 1.40,
    "5. Tortillas": 3.25
}

# Mostrar el menú
print("Menú de Comidas:")
print("-" * 30)
for comida, precio in menu.items():
    print(f"{comida} - ${precio:.2f}")
print("-" * 30)

# Solicitar al usuario que elija un plato
eleccion = input("Introduce el número del plato que deseas pedir: ")

# Verificar si la elección está en el menú
opciones = list(menu.keys())
if eleccion.isdigit() and int(eleccion) in range(1, len(opciones) + 1):
    plato_seleccionado = opciones[int(eleccion) - 1]
    precio_total = menu[plato_seleccionado]
    print(f"Has elegido: {plato_seleccionado.split('. ')[1]}")
    print(f"El precio total es: ${precio_total:.2f}")
else:
    print("Elección inválida. Por favor, elige un plato del menú.")




# Ejercicio número 5
def calcular_cuadrado(numero):
    return numero ** 2
numero_entero = int(input("Ingrese un número entero del 1 al 20: "))
resultado = calcular_cuadrado(numero_entero)
print("El cuadrado de", numero_entero, "es:", resultado)