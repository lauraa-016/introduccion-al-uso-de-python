"""
6. Añade a todas las películas cuya edad recomendada sea 0 el género “Infantil”.
"""

from datos import peliculas

for pelicula in peliculas:
    if pelicula["edad_recomendada"] == 0:
        pelicula["generos"].append("Infantil")