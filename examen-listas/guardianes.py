from datos import personajes

def ejercicio1():
    personaje_nuevo = {
        "nombre": "Pepe Rodríguez",
        "raza": "Humano",
        "ocupacion": "Vampiro",
        "estilo_combate":["Respiracion del Agua", "Respiracion del Sol"],
        "atributos":{
            "fuerza":100, "defensa":50, "velocidad":65
        }
    }

    personajes.append(personaje_nuevo)
    print(personajes)

def ejercicio2():
    
    media = 0

    for personaje in personajes:
        atributos = personaje["atributos"]
        
        media = (
            atributos["fuerza"] + atributos["defensa"] + atributos["velocidad"]
        ) / 3

        if media > 85:
            print(personaje)


def ejercicio3():
    suma = 0

    for personaje in personajes:
        suma += personaje["atributos"]["fuerza"]
    
    media = suma / len(personajes)

    for personaje in personajes:
        if personaje["atributos"]["velocidad"] > media:
            print(personaje)

def ejercicio4():
    for personaje in personajes:
        if "Respiracion del Agua" in personaje["estilo_combate"]:
            defensa = personaje["atributos"]["defensa"]
            personaje["atributos"]["defensa"] = min(defensa + 10, 100)

    for personaje in personajes:
        print(f"{personaje["nombre"]} {personaje["atributos"]["defensa"]}")

def ejercicio5():
    zenitsu_agatsuma ={
        "nombre": "Zenitsu Agatsuma",
        "raza": "Humano",
        "ocupacion": "Cazador de demonios",
        "estilo_combate":["Respiracion del Agua", "Respiracion del Sol"],
        "atributos":{
            "fuerza":200, "defensa":88, "velocidad":90
        }
    }

    for personaje in personajes:
        defensa = personaje["atributos"]["defensa"]
        if defensa < zenitsu_agatsuma["atributos"]["fuerza"]:
            print(f"{personaje["nombre"]} {personaje["atributos"]["fuerza"]} {personaje["atributos"]["defensa"]}")

def ejercicio6():
    for personaje in personajes:
        if personaje["ocupacion"] == "Cazador de demonios":
            personajes.remove(personaje)

    for personaje in personajes:
        print(personajes)
