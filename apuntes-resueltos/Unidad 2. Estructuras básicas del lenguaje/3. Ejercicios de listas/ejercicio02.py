"""
Muestra la media de altura de todos los pokémons.
"""

from datos import pokemons

suma_alturas = 0

for pokemon in pokemons:
    suma_alturas = suma_alturas + pokemon["altura_m"]

media = suma_alturas / len(pokemons)
media = round(media,2)

print(f"La media de altura es {media}")