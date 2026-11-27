def convertir_acciones(compania : str, num_acciones: int, monedaCambio: str)->float:
    if num_acciones < 0:
        raise ValueError("El número de acciones no puede ser negativo.")

    compania = compania.upper() 
    monedaCambio = monedaCambio.lower()

    if compania == "NVDA":
        valor_accion = 156.20
    elif compania == "SONY":
        valor_accion = 24.16
    elif compania == "BMW":
        valor_accion = 58.12
    else:
        raise ValueError("Compañía no válida.")

    total_euros = valor_accion * num_acciones

    if monedaCambio == "euro":
        resultado = total_euros
    elif monedaCambio == "dolar":
        resultado = total_euros * 1.10
    elif monedaCambio == "libra":
        resultado = total_euros * 0.83
    else:
        raise ValueError("Moneda no válida.")

    return float(round(resultado, 2))