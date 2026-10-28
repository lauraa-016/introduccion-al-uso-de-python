"""
4. Muestra una lista de tuplas (titulo_serie, nota_dada) de las reseñas dejadas por el
usuario Elena.
"""
from datos import series

resenas_elena = [(s["titulo"], r["nota"]) for s in series for r in s["reseñas"] if r["usuario"] == "Elena"]

print(resenas_elena)