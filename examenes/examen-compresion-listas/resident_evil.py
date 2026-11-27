from datos import personajes

def ejercicio1():
    nombres_policia = [
        p["nombre"] for p in personajes 
        if p["afiliacion"] == "Policía de Raccoon City" 
        and p["vivo"]
    ]
    print(nombres_policia)

def ejercicio2():
    resultado = [
        p["nombre"]
        for p in personajes
        if p["afiliacion"] == "Policía de Raccoon City"
        and "Pistola Samurai Edge" in p["armas"]
        and "Lanzagranadas" in p["armas"]
    ]
    print(resultado)

def ejercicio3():
    resultado = [
        (p["nombre"], p["afiliacion"])
        for p in personajes
        if p["afiliacion"] != "Policía de Raccoon City"
    ]
    print(resultado)

def ejercicio4():
    resultado = [
        p["nombre"] + " (" + p["afiliacion"] + ")"
        for p in personajes
        if p["registro_misiones"]["misiones_completadas"] >= 20
    ]
    print(resultado)

def ejercicio5():
    resultado = [
        (p["nombre"], p["estatura_m"] * 100)
        for p in personajes
        if p["estatura_m"] > 1.70
    ]
    print(resultado)

def ejercicio6():
    resultado = [
        arma
        for p in personajes
        for arma in p["armas"]
    ]
    print(resultado)

def ejercicio7():
    resultado = [
        p["nombre"]
        for p in personajes
        if p["registro_misiones"]["zombies_solo"]
        + p["registro_misiones"]["zombies_equipo"] >= 100
    ]
    print(resultado)

def ejercicio8():
    resultado = [
        {
            "nombre": p["nombre"],
            "zombies_totales": (
                p["registro_misiones"]["zombies_solo"]
                + p["registro_misiones"]["zombies_equipo"]
            )
        }
        for p in personajes
    ]
    print(resultado)

def ejercicio9():
    alturas = [p["estatura_m"] for p in personajes]

    media = sum(alturas) / len(alturas)

    print(media)

def ejercicio10():
    alturas = [p["estatura_m"] for p in personajes]

    media = sum(alturas) / len(alturas)

    resultado = [
        (p["nombre"], p["estatura_m"])
        for p in personajes
        if p["estatura_m"] > media
    ]
    print(resultado)