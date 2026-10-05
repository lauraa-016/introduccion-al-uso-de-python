"""
Dada la lista de videojuegos que se encuentra en el anexo I, muestra por pantalla
solo los videojuegos cuyo título empiece por M.
videojuegos = ("Super Mario Bros", "New Super Mario Bros", "Mario vs Luigi", "Mario Kart")
"""

videojuegos = ("Super Mario Bros", "New Super Mario Bros", "Mario vs Luigi", "Mario Kart")

print("Videojuegos que empiezan con 'M':")

for juego in videojuegos:
    if juego.startswith("M"):
        print(juego)