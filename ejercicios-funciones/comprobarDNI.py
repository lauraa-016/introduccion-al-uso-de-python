"""
1. Crea una función llamada comprobarLetraDNI que reciba una cadena de
caracteres que representará al DNI de una persona y devuelva True si el DNI
es correcto y False si no lo es. Un DNI es correcto si tiene 8 dígitos enteros
seguidos de una letra (mayúscula o minúscula), y la letra es correcta. Para
conocer si la letra es correcta puedes consultar la web del Ministerio del
Interior.
"""
def comprobarLetraDNI(dni):

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    if len(dni) != 9:
        return False

    numero = ""

    for i in range(8):
        if not dni[i].isdigit():
            return False
        numero += dni[i]

    if not dni[8].isalpha():
        return False

    numero = int(numero)
    resto = numero % 23

    return dni[8].upper() == letras[resto]

print(comprobarLetraDNI("12345678Z"))
print(comprobarLetraDNI("12345678A"))
print(comprobarLetraDNI("1234567"))