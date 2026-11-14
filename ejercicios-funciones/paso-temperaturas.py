"""
2. Crea una función llamada convertirTemperatura que reciba un número con
decimales y dos cadenas de caracteres. Las cadenas de caracteres posibles
serán “C”, “K” y “F”, que representan unidades de temperatura (Celsius,
Kelvin y Fahrenheit). La función devolverá, como número con decimales, el
resultado de convertir de la primera unidad que reciba la función a la
segunda. Por ejemplo, convertirTemperatura(10,”F”,”C”) devolvería el
resultado de pasar 10 Fahrenheit a Celsius. Devuelve el resultado con dos
decimales, redondeando al valor más cercano.
"""
def convertirTemperatura(temperatura, unidadOrigen, unidadDestino):

    # convierto a celsius primero
    if unidadOrigen == "C":
        celsius = temperatura
    elif unidadOrigen == "K":
        celsius = temperatura - 273.15
    elif unidadOrigen == "F":
        celsius = (temperatura - 32) * 5 / 9

    # de celsius a otra unidad
    if unidadDestino == "C":
        resultado = celsius
    elif unidadDestino == "K":
        resultado = celsius + 273.15
    elif unidadDestino == "F":
        resultado = celsius * 9 / 5 + 32

    return round(resultado, 2)

print(convertirTemperatura(10, "F", "C"))