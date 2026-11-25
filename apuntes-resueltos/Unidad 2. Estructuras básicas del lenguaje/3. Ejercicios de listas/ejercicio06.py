"""
Inserta al final de la lista un nuevo pokémon que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables).
"""

from datos import pokemons

nuevo_pokemon = {
        "nombre": "Mewtwo",
        "generacion": 3,
        "categoria": "Ovo",
        "tipos": ["Psíquico"],
        "peso_kg": 60.3,
        "altura_m": 3.2
}

pokemons.append(nuevo_pokemon)

print(pokemons)