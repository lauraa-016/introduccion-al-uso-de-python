"""
3. Muestra una lista con los nombres de los jugadores que pertenecen al "FC
Barcelona".
"""
from datos import jugadores

fc_barcelona = [f for f in jugadores if f["equipo"] == "FC Barcelona"]

print(fc_barcelona)
