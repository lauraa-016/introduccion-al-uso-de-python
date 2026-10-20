"""
2. Muestra el título y la duración de las películas con más duración que la media. Hazlo
con el formato título duración (por ejemplo: El Señor de los Anillos: La
Comunidad del Anillo 178).
"""

from datos import peliculas

duracion_total = 0

for pelicula in peliculas:
    duracion_total += pelicula["duracion"]

duracion_media = duracion_total / len(peliculas)

for pelicula in peliculas:
    if pelicula["duracion"] > duracion_media:
        print(f"{pelicula["titulo"]}, {pelicula["duracion"]}")