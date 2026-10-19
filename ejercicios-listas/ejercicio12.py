"""
12. Elimina todos los personajes cuya raza sea demonio.
"""

from datos import personajes_frieren

print("Personajes con demonios:", len(personajes_frieren))

for personaje in personajes_frieren[:]: # [:] para hacer una copia de la lista para no comernos nada en la segunda iteración cuando borra algo
    if personaje["raza"] == "Demonio":
        personajes_frieren.remove(personaje)

print("Personajes sin demonios:", len(personajes_frieren))