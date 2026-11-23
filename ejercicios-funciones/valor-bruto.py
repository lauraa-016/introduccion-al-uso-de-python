"""
3. Crea una función llamada calcularValorBruto, que reciba un número con
decimales (el precio de un producto) y una cadena de caracteres (que
representará el tipo de IVA aplicable). Las cadenas de caracteres posibles
serán GENERAL, REDUCIDO y SUPERREDUCIDO. La función devolverá el
resultado de sumar el IVA aplicable al valor neto del producto. Por ejemplo,
calcularValorBruto(10,”GENERAL”) devolvería el resultado de sumar a los
10€ de valor neto, el porcentaje de IVA del tipo general (que es un 21%), lo
que daría 12,1€. Devuelve el resultado con dos decimales, redondeando
hacia arriba.
"""
import math

def calcularValorBruto(precio, tipoIVA):

    if tipoIVA == "GENERAL":
        porcentaje = 0.21
    elif tipoIVA == "REDUCIDO":
        porcentaje = 0.10
    elif tipoIVA == "SUPERREDUCIDO":
        porcentaje = 0.04

    # el iva
    resultado = precio * (1 + porcentaje)

    # dos decimales arriba (ahce falta math)
    resultado = math.ceil(round(resultado * 100, 10)) / 100

    return resultado

print(calcularValorBruto(10, "GENERAL"))
print(calcularValorBruto(10, "REDUCIDO"))
print(calcularValorBruto(10, "SUPERREDUCIDO"))