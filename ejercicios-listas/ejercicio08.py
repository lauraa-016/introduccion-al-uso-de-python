from datos import personajes_frieren

suma_edades = 0
n_humanos = 0

for personaje in personajes_frieren:
    if personaje["raza"] == "Humano":
        suma_edades += personaje["edad"]
        n_humanos += 1

media = suma_edades / n_humanos
print(media)