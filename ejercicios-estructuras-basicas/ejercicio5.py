"""
Pedir al usuario dos números enteros y mostrar los números pares dentro de dicho
intervalo. Si el primer número es mayor que el segundo se mostrará por pantalla un
mensaje de error. Realizar una versión con FOR y otra con WHILE.
"""
numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

# Versión con FOR
if numero1 > numero2:
    print("Error: El primer número no puede ser mayor que el segundo.")
else:
    print("Números pares en el intervalo:")
    for i in range(numero1, numero2 + 1):
        if i % 2 == 0:
            print(i)

# Versión con WHILE
if numero1 > numero2:
    print("Error: El primer número no puede ser mayor que el segundo.")
else:
    print("Números pares en el intervalo:")
    i = numero1
    while i <= numero2:
        if i % 2 == 0:
            print(i)
        i += 1