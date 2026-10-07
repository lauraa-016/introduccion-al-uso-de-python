"""
4. Muestra el nombre y los tipos de los pokémons que sean de tipo agua.
"""
from datos import pokemons

for pokemon in pokemons:
    if "Agua" in pokemon["tipos"]:
        print(pokemon["nombre"], "es de tipo agua y sus tipos son:", pokemon["tipos"])