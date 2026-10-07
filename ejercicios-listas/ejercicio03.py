"""
3. Muestra el nombre y la altura de todos los pokémons que midan menos que la
media.
"""
from datos import pokemons

total_altura = 0

for pokemon in pokemons:
    total_altura += pokemon["altura_m"]

media_altura = total_altura / len(pokemons)

print("Los pokémons que miden menos que la media de altura son :")
for pokemon in pokemons:
    if pokemon["altura_m"] < media_altura:
        print(f"{pokemon['nombre']} mide {pokemon['altura_m']} m.")
