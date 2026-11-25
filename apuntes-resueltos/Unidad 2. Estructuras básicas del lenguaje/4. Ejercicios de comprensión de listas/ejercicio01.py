"""
Muestra una lista solo con los nombres de todos los futbolistas.
"""

from datos import jugadores

nombres_futbolistas = [j["nombre"] for j in jugadores]

print(nombres_futbolistas)