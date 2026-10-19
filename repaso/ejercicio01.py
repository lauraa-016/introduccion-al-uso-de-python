"""
1. Añade una película a la lista (con todos los datos completos).
"""

from peliculas import peliculas

nueva_pelicula = {
"titulo": "IT",
"duracion": 148,
"año_estreno": 2010,
"edad_recomendada": 13,
"generos": ["Ciencia ficción", "Terror", "Intriga"]
}

peliculas.append(nueva_pelicula)