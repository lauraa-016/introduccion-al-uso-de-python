def convertirTemperatura(temperatura_inicial : float, unidad_inicial : str, unidad_final : str) -> float:
    """Convierte una temperatura de la unidad inicial especificada a la unidad final especificada

    Args:
        temperatura_inicial (float): La temperatura desde la que queremos convertir a otra unidad
        unidad_inicial (str): La unidad en la que se encuentra la temperatura inicial
        unidad_final (str): La unidad en la que queremos convertir la temperatura inicial

    Returns:
        float: La temperatura en la unidad final indicada
    """
    unidad_inicial = unidad_inicial.upper()
    unidad_final = unidad_final.upper()

    if unidad_inicial not in ["C", "K", "F"] or unidad_final not in ["C", "K", "F"]:
        raise ValueError("La unidad inicial debe ser C, K o F")

    temperatura_final = 0

    if unidad_inicial == "C":
        if temperatura_inicial < -273.15:
            raise ValueError("La temperatura inicial no puede ser inferior a -273,15 Celsius")
        if unidad_final == "F":
            temperatura_final = (temperatura_inicial * (9/5)) + 32
        elif unidad_final == "K":
            temperatura_final = temperatura_inicial + 273.15
    elif unidad_inicial == "F":
        if temperatura_inicial < -459.67:
            raise ValueError("La temperatura inicial no puede ser inferior a -459,67 Fahrenheit")
        if unidad_final == "C":
            temperatura_final = (temperatura_inicial - 32) * (5/9)
        elif unidad_final == "K":
            temperatura_final = ((temperatura_inicial - 32) * (5/9)) + 273
    elif unidad_inicial == "K":
        if temperatura_inicial < 0:
            raise ValueError("La temperatura inicial no puede ser inferior a 0 Kelvin")
        if unidad_final == "F":
            temperatura_final = (temperatura_inicial - 273.15) * (9/5)
        elif unidad_final == "C":
            temperatura_final = temperatura_inicial - 273.15

    return round(temperatura_final,2)

print(convertirTemperatura(24,"K","F"))