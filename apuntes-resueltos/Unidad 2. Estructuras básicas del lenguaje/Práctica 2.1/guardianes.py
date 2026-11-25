from datos import personajes

def ejercicio1():
    nuevo_personaje = {
        "nombre" : "Mbappé",
        "raza" : "Humano",
        "ocupacion" : "Dictador",
        "estilo_combate" : ["Respiración del Agua"],
        "atributos" : {"fuerza" : 89, "defensa" : 68, "velocidad" : 94}
    }
    personajes.append(nuevo_personaje)

def ejercicio2():
    for personaje in personajes:
        media = (personaje["atributos"]["fuerza"] + personaje["atributos"]["defensa"] + personaje["atributos"]["velocidad"]) / 3
        if media > 85:
            print(personaje)

def ejercicio3():
    suma_fuerzas = 0
    for personaje in personajes:
        suma_fuerzas += personaje["atributos"]["fuerza"]

    media_fuerzas = suma_fuerzas / len(personajes)

    for personaje in personajes:
        if personaje["atributos"]["fuerza"] > media_fuerzas:
            print(personaje)

def ejercicio4():
    for personaje in personajes:
        for estilo in personaje["estilo_combate"]:
            if estilo == "Respiración del Agua":
                personaje["atributos"]["defensa"] += 10
                if personaje["atributos"]["defensa"] > 100:
                    personaje["atributos"]["defensa"] = 100
        print(personaje["nombre"], personaje["atributos"]["defensa"])

def ejercicio5():
    fuerza_zenitsu = 0

    for personaje in personajes:
        if personaje["nombre"] == "Zenitsu Agatsuma":
            fuerza_zenitsu = personaje["atributos"]["fuerza"]

    for personaje in personajes:
        if personaje["nombre"] != "Zenitsu Agatsuma":
            if personaje["atributos"]["defensa"] < fuerza_zenitsu:
                print(personaje["nombre"], personaje["atributos"]["fuerza"], personaje["atributos"]["defensa"])

def ejercicio6():
    for personaje in personajes[:]:
        if personaje["ocupacion"] == "Cazador de Demonios":
            personajes.remove(personaje)