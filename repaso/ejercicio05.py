"""
5. Muestra el título y la edad recomendada de las películas cuya edad recomendada
esté entre 7 y 13. Hazlo con el formato título edad_recomendad (por ejemplo El
Padrino 18).
"""

from datos import peliculas

for pelicula in peliculas:
    if pelicula["edad_recomendada"] >= 7 and pelicula["edad_recomendada"] <= 13:
        print(f"{pelicula["titulo"]} {pelicula["edad_recomendada"]}")
