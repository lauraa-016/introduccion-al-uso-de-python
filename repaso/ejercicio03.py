"""
3. A todas las películas que sean del género Drama, cámbiale la edad recomendada a
18.
"""

from datos import peliculas

for pelicula in peliculas:
    if "Drama" in pelicula["generos"]:
        pelicula["edad_recomendada"] = 18

print(peliculas)
