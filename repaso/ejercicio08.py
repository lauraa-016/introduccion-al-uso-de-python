"""
8. Borra todas las películas cuya edad recomendada sea 0.
"""

from datos import peliculas

for pelicula in peliculas:
    if pelicula["edad_recomendada"] == 0:
        peliculas.remove(pelicula)

print(peliculas)