from datos import personajes

media = 0

for personaje in personajes:
    atributos = personaje["atributos"]
    
    media = (
        atributos["fuerza"] + atributos["defensa"] + atributos["velocidad"]
    ) / 3

    if media > 85:
        print(personaje)