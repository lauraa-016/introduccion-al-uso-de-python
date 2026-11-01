"""
6. Muestra una lista de cadenas con el formato “La serie {titulo} tiene {n} reseñas”, para
todas las series.
"""
from datos import series

lista_cadenas = [
    f"La serie {serie['titulo']} tiene {len(serie['reseñas'])} reseñas"
    for serie in series
]

print(lista_cadenas)