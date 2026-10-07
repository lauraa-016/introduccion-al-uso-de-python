"""
5. Muestra los pokémons que tengan un tipo que acabe en “a”.
"""
from datos import pokemons

for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        if tipo.endswith("a"):
            print(pokemon['nombre'], "tiene un tipo que acaba en 'a':", tipo)