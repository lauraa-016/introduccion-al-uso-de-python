"""
Extrae en una única lista todas las filigranas de todos los jugadores (no importa si
hay duplicadas) y muéstrala.
"""

from datos import jugadores

lista = [f for j in jugadores for f in j["filigranas"]]
print(lista)

# para quitar duplicados (opcional)
#lista2 = []
#for f in lista:
#    if f not in lista2:
#        lista2.append(f)
#print(lista2)