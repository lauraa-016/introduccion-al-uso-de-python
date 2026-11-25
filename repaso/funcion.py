
def convertir_acciones(compania, numero_acciones, moneda_cambio):

    # Tabla 1: valor de las acciones en euros
    empresas = {
        "NVDA": 156.20,
        "SONY": 24.16,
        "BMW": 58.12
    }

    # Tabla 2: tipos de cambio
    cambios = {
        "euro": 1,
        "dolar": 1.10,
        "libra": 0.83
    }

    # Convertimos los datos a mayúsculas y minúsculas
    compania = compania.upper()
    moneda_cambio = moneda_cambio.lower()

    # Calculamos el valor total de las acciones en euros
    resultado = empresas[compania] * numero_acciones

    # Convertimos a la moneda indicada
    resultado = resultado * cambios[moneda_cambio]

    # Redondeamos a dos decimales
    return round(resultado, 2)

print(convertir_acciones("NVDA", 10, "euro"))
print(convertir_acciones("SONY", 5, "dolar"))
print(convertir_acciones("BMW", 20, "libra"))