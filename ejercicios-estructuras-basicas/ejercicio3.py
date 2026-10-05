"""
Pedir al usuario la edad de una persona y mostrar si es mayor o menor de edad. Si
la edad es menor a 0 mostrar un mensaje de error, y si es superior a 120 indicar que
es un vampiro.
"""
edad = int(input("Introduce tu edad: "))

# version con if-elif-else
if edad < 0:
    print("Error: La edad no puede ser negativa.")
elif edad < 18:
    print("Eres menor de edad.")
elif edad > 120:
    print("Eres un vampiro.")
else:
    print("Eres mayor de edad.")

# version con match-case    
match edad:
    case _ if edad < 0:
        print("Error: La edad no puede ser negativa.")
    case _ if edad < 18:
        print("Eres menor de edad.")
    case _ if edad > 120:
        print("Eres un vampiro.")
    case _:
        print("Eres mayor de edad.")
        
