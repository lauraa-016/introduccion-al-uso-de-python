"""
2. Muestra la lista de los jugadores que llevan el dorsal número 10.
"""
from datos import jugadores

futbolistas_dorsal_10 = [f for f in jugadores if f["dorsal"] == 10]

print(futbolistas_dorsal_10)