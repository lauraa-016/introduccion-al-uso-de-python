"""
6. Inserta al final de la lista un nuevo pokémon que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables).
"""
from datos import pokemons

pokemon_nuevo = {
    "nombre": "Pikachu",
    "tipos": ["Eléctrico"],
    "altura_m": 0.4,
    "peso_kg": 6.0
}

pokemons.append(pokemon_nuevo)
