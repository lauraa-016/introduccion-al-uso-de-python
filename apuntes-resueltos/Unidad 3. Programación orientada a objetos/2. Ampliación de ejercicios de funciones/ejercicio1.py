def sumatorio(numero : int) -> int:
    sumatorio = 0
    for i in range(1,numero+1):
        sumatorio += i
    return sumatorio

def factorial(numero : int) -> int:
    factorial = 1
    for i in range(1,numero+1):
        factorial *= i
    return factorial

def aplicar_funcion(funcion : str, numero : int) -> int:
    """Devuelve el resultado de aplicar la funcion indicada con el numero especificado

    Args:
        funcion (str): La funcion que queremos ejecutar
        numero (int): El numero que queremos pasar por parametro a la funcion

    Returns:
        (int): El resultado de aplicar la función con el número
    """

    funcion = funcion.lower()
    if funcion not in ["sumatorio", "factorial"]:
        raise ValueError("Las unicas funciones soportadas son sumatorio y factorial")

    if numero < 0:
        raise ValueError("El número debe ser superior o igual a cero")

    resultado = 0
    if funcion == "sumatorio":
        resultado = sumatorio(numero)
    elif funcion == "factorial":
        resultado = factorial(numero)

    return resultado

print(aplicar_funcion("factorial",4))