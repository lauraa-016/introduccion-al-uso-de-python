"""
2. Muestra la media de altura de todos los pokémons.
"""
from datos import pokemons

total_altura = 0

for pokemon in pokemons:
    total_altura += pokemon["altura_m"]

media_altura = total_altura / len(pokemons)
print(f"La media de altura de todos los pokémons es {media_altura} metros.")