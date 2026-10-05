""""
A partir de 60 mm de lluvia acumulados en 12 horas se declara una alerta amarilla, y
a partir de 120 mm, una alerta roja. Pedir al usuario los milímetros de lluvia
acumulados y mostrar por pantalla si No hay alerta, Hay alerta amarilla o Hay
alerta roja. Realizar una versión con IF y otra con MATCH.
"""
lluvia = float(input("Introduce los milímetros de lluvia acumulados en 12 horas: "))

# Versión con IF
if lluvia < 60:
    print("No hay alerta.")
elif lluvia < 120:
    print("Hay alerta amarilla.")
else:
    print("Hay alerta roja.")

# Versión con MATCH
match lluvia:
    case _ if lluvia < 60:
        print("No hay alerta.")
    case _ if lluvia < 120:
        print("Hay alerta amarilla.")
    case _:
        print("Hay alerta roja.")
