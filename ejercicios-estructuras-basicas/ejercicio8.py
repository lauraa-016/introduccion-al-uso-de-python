"""
Dada la lista de videojuegos que se encuentra en el anexo II, muestra por pantalla
solo los videojuegos que cuesten más de 20€.
videojuegos = [

{"titulo": "The Legend of Zelda: BOTW", "consola": "Nintendo Switch", "precio": 59.99},
{"titulo": "Hollow Knight", "consola": "PC", "precio": 14.99},
{"titulo": "Stardew Valley", "consola": "PlayStation 4", "precio": 13.99},
{"titulo": "Assassin's Creed Shadows", "consola": "PlayStation 5", "precio": 69.99},
{"titulo": "Resident Evil: Requiem", "consola": "PlayStation 5", "precio": 79.99},
{"titulo": "Trails in the Sky 1st Chapter", "consola": "Nintendo Switch", "precio": 49.9}
]
"""

videojuegos = [
    {"titulo": "The Legend of Zelda: BOTW", "consola": "Nintendo Switch", "precio": 59.99},
    {"titulo": "Hollow Knight", "consola": "PC", "precio": 14.99},
    {"titulo": "Stardew Valley", "consola": "PlayStation 4", "precio": 13.99},
    {"titulo": "Assassin's Creed Shadows", "consola": "PlayStation 5", "precio": 69.99},
    {"titulo": "Resident Evil: Requiem", "consola": "PlayStation 5", "precio": 79.99},
    {"titulo": "Trails in the Sky 1st Chapter", "consola": "Nintendo Switch", "precio": 49.9}
]

print("Videojuegos que cuestan más de 20€:")

for juego in videojuegos:
    if juego["precio"] > 20:
        print(f"- {juego['titulo']} ({juego['consola']}): {juego['precio']}€") # f es para formatear la cadena y mostrar el título, consola y precio sin tener que concatenar todo

# línea sin el formato:
# print("- " + juego["titulo"] + " (" + juego["consola"] + "): " + str(juego["precio"]) + "€")