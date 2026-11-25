def convertir_acciones(compania: str, num_acciones: int, moneda: str) -> float:
    if not isinstance(compania, str):
        raise TypeError("La compañía debe ser una cadena de texto.")
    if not isinstance(num_acciones, int):
        raise TypeError("El número de acciones debe ser un entero.")
    if not isinstance(moneda, str):
        raise TypeError("La moneda de cambio debe ser una cadena de texto.")

    if num_acciones < 0:
        raise ValueError("El número de acciones no puede ser negativo.")

    compania = compania.upper()
    moneda = moneda.lower()

    if compania == "NVDA":
        valor_accion = 156.20
    elif compania == "SONY":
        valor_accion = 24.16
    elif compania == "BMW":
        valor_accion = 58.12
    else:
        raise ValueError("Compañía no válida.")

    total_euros = valor_accion * num_acciones

    if moneda == "euro":
        resultado = total_euros
    elif moneda == "dolar":
        resultado = total_euros * 1.10
    elif moneda == "libra":
        resultado = total_euros * 0.83
    else:
        raise ValueError("Moneda no válida.")

    return float(round(resultado, 2))