
from datos import personajes


# EJERCICIO 1
# Nombres de los personajes vivos que pertenecen
# al Cuerpo de Exploración.

def ejercicio1():
    resultado = [
        p["nombre"]
        for p in personajes
        if p["afiliacion"] == "Cuerpo de Exploración" and p["vivo"]
    ]

    print("\nEJERCICIO 1")
    print(resultado)


# EJERCICIO 2
# Nombres de los personajes del Cuerpo de Exploración
# que tienen las habilidades Supervivencia y Sigilo.

def ejercicio2():
    resultado = [
        p["nombre"]
        for p in personajes
        if p["afiliacion"] == "Cuerpo de Exploración"
        and "Supervivencia" in p["habilidades"]
        and "Sigilo" in p["habilidades"]
    ]

    print("\nEJERCICIO 2")
    print(resultado)


# EJERCICIO 3
# Tuplas con el nombre y la afiliación de los personajes
# que no pertenecen al Cuerpo de Exploración.

def ejercicio3():
    resultado = [
        (p["nombre"], p["afiliacion"])
        for p in personajes
        if p["afiliacion"] != "Cuerpo de Exploración"
    ]

    print("\nEJERCICIO 3")
    print(resultado)


# EJERCICIO 4
# Nombre y afiliación entre paréntesis de los personajes
# que han completado 20 misiones o más.

def ejercicio4():
    resultado = [
        p["nombre"] + " (" + p["afiliacion"] + ")"
        for p in personajes
        if p["registro_combate"]["misiones_completadas"] >= 20
    ]

    print("\nEJERCICIO 4")
    print(resultado)


# EJERCICIO 5
# Tuplas con los nombres y las alturas en centímetros
# de los personajes que miden más de 1,70 metros.

def ejercicio5():
    resultado = [
        (p["nombre"], p["estatura_m"] * 100)
        for p in personajes
        if p["estatura_m"] > 1.70
    ]

    print("\nEJERCICIO 5")
    print(resultado)


# EJERCICIO 6
# Lista aplanada con todas las habilidades de los personajes.
# Se permiten habilidades repetidas.

def ejercicio6():
    resultado = [
        habilidad
        for p in personajes
        for habilidad in p["habilidades"]
    ]

    print("\nEJERCICIO 6")
    print(resultado)


# EJERCICIO 7
# Nombres de los personajes que han matado 5 o más titanes
# sumando los que han matado solos y en equipo.

def ejercicio7():
    resultado = [
        p["nombre"]
        for p in personajes
        if p["registro_combate"]["titanes_solo"]
        + p["registro_combate"]["titanes_equipo"] >= 5
    ]

    print("\nEJERCICIO 7")
    print(resultado)


# EJERCICIO 8
# Lista de diccionarios con el nombre y el número total
# de titanes eliminados por cada personaje.

def ejercicio8():
    resultado = [
        {
            "nombre": p["nombre"],
            "titanes_totales": (
                p["registro_combate"]["titanes_solo"]
                + p["registro_combate"]["titanes_equipo"]
            )
        }
        for p in personajes
    ]

    print("\nEJERCICIO 8")
    print(resultado)


# EJERCICIO 9
# Calcular la media de las alturas de todos los personajes.

def ejercicio9():
    alturas = [p["estatura_m"] for p in personajes]

    media = sum(alturas) / len(alturas)

    print("\nEJERCICIO 9")
    print("La media de las alturas es:", media)


# EJERCICIO 10
# Calcular la media de las alturas y mostrar una lista
# de tuplas con los personajes que superan esa media.

def ejercicio10():
    media = [
        sum([p["estatura_m"] for p in personajes]) / len(personajes)
    ][0]

    resultado = [
        (p["nombre"], p["estatura_m"])
        for p in personajes
        if p["estatura_m"] > media
    ]

    print("\nEJERCICIO 10")
    print(resultado)
