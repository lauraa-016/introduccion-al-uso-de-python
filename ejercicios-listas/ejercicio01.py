"""
Dada la lista del Anexo I, realiza los siguientes ejercicios de listas:
"""
from datos import pokemons

# 1. Muestra en una sóla línea el nombre y el peso del pokémon con más peso.
pokemon_mas_pesado = pokemons[0]

for pokemon in pokemons:
    if pokemon["peso_kg"] > pokemon_mas_pesado["peso_kg"]:
        pokemon_mas_pesado = pokemon

print("El Pokémon con más peso es", pokemon_mas_pesado['nombre'], "con un peso de ", pokemon_mas_pesado['peso_kg'], "kg.")