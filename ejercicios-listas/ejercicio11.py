"""
11. Inserta al final de la lista un nuevo personaje que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables).
"""

from datos import personajes_frieren

nuevo_personaje = {
"nombre": "Pepe",
"raza": "Elfo",
"clase": "Mago",
"edad": 500,
"afiliacion": ["Magos de Primera Clase"]
},

personajes_frieren.append(nuevo_personaje)