"""
5. Muestra la lista de los jugadores que saben hacer la filigrana "ruleta".
"""
from datos import jugadores

lista_ruleta = [j for j in jugadores if "ruleta" in j["filigranas"] ]

print(lista_ruleta)