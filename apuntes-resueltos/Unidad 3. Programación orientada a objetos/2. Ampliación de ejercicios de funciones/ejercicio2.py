animales = [
    ["Lobo ibérico", "Mamífero", 2500],
    ["Lince ibérico", "Mamífero", 1668],
    ["Quebrantahuesos", "Ave", 2000],
    ["Oso pardo", "Mamífero", 500]
]

def comprobar_estado(especie : str) -> str:
    """Comprueba el estado en que se encuentra una especie de animales

    Args:
        especie (str): La especie que queremos comprobar

    Returns:
        (str): Una cadena de caracteres indicando su estado
    """
    estado = ""
    encontrado = False
    for animal in animales:
        if animal[0].lower() == especie.lower():
            encontrado = True
            if animal[2] == 0:
                estado = "Extinto"
            elif animal[2] <= 500:
                estado = "En peligro crítico"
            elif animal[2] > 500 and animal[2] <= 2000:
                estado = "En peligro"
            else:
                estado = "Amenazado"
            break
    if encontrado == False:
        raise ValueError("No se ha encontrado el personaje")

    return estado