import math

GENERAL = 0.21
REDUCIDO = 0.10
SUPERREDUCIDO = 0.04

def calcularValorBruto(valor_neto : float, tipo_iva : str) -> float:
    """Calcula el valor bruto de un producto en base a su valor neto y el tipo de IVA aplicado

    Args:
        valor_neto (float): El valor neto del producto, en euros
        tipo_iva (str): El tipo de IVA aplicable, que puede ser general, reducido o superreducido

    Returns:
        float: El valor bruto del producto tras aplicar el IVA
    """
    tipo_iva = tipo_iva.lower()
    if tipo_iva not in ["general", "reducido", "superreducido"]:
        raise ValueError("El tipo de IVA solo puede ser general, reducido o superreducido")

    if valor_neto < 0:
        raise ValueError("El valor neto no puede ser negativo")

    valor_bruto = 0
    if tipo_iva == "general":
        valor_bruto = (valor_neto * GENERAL) + valor_neto
    elif tipo_iva == "reducido":
        valor_bruto = (valor_neto * REDUCIDO) + valor_neto
    elif tipo_iva == "superreducido":
        valor_bruto = (valor_neto * SUPERREDUCIDO) + valor_neto

    return math.ceil(valor_bruto)

print(calcularValorBruto(10,"General"))