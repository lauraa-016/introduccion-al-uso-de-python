"""
7. Crea una copia de la lista llamada peliculas_infantiles e incluye en ella todas las
películas que tengan el género Infantil.
"""
from datos import peliculas

peliculas_infantiles = []

for pelicula in peliculas:
    if pelicula["edad_recomendada"] == 0:
        pelicula["generos"].append("Infantil")

for pelicula in peliculas:
    if "Infantil" in pelicula["generos"]:
        peliculas_infantiles.append(pelicula)
