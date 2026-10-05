"""
Supongamos que la contraseña para acceder es “12345”. Pedir al usuario la
contraseña por pantalla y, si es la correcta, mostrar un mensaje de bienvenida. Si la
contraseña introducida es incorrecta, volver a pedirla hasta que se introduzca
correctamente.
"""
contraseña_correcta = "12345"
contraseña_introducida = input("Introduce la contraseña: ")

while contraseña_introducida != contraseña_correcta:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    contraseña_introducida = input("Introduce la contraseña: ")

print("Bienvenido.")