"""
Pedir al usuario un número entero y calcular el factorial desde 1 hasta
dicho número (incluido). Si el número introducido es menor que 1, 
mostrar un mensaje de error.
"""

factorial = 1
numero = int(input("Número: "))

if numero < 1:
    print("Error")
else:
    i = 1
    while i <= numero:
        factorial = factorial * i
        i = i + 1

print(factorial)