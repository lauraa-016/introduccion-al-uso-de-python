# 9. Muestra el nombre y la raza de todos los personajes que sean magos de primera
# clase. 

from datos import personajes_frieren

for personaje in personajes_frieren:
    if personaje["clase"] == "Mago" and "Magos de Primera Clase" in personaje["afiliacion"]:
        print(personaje["nombre"] + " " + personaje["raza"])

