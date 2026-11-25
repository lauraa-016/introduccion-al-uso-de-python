def comprobarDNI(dni :str) -> bool:
    """Comprueba si un DNI es válido

    Args:
        dni (str): El DNI que queremos comprobar

    Returns:
        (bool): Si el DNI es válido o no
    """
    valido = True

    if len(dni) != 9:
        valido = False

    numero = dni[:8]

    if not numero.isdigit():
        valido = False

    numero = int(numero)

    resto = numero % 23

    letra = dni[8].upper()
    letrasPosibles = "TRWAGMYFPDXBNJZSQVHLCKE"

    if letra != letrasPosibles[resto]:
        valido = False

    return valido

print(comprobarDNI("12345678Z"))