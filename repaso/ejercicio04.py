"""
4. Muestra el título y la duración de todas las películas que sean de Fantasía y
Aventura al mismo tiempo. Hazlo con el formato del ejercicio 2.
"""

from datos import peliculas

for pelicula in peliculas:
    if "Fantasía" in pelicula["generos"]:
        if "Aventura" in pelicula["generos"]:
            print(f"{pelicula["titulo"]}, {pelicula["duracion"]}")