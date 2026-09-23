def main():
    lista = ["manzana", "pera", "melocoton"]
    lista2 = ["kiwi", "sandia", "melon"] 

    lista.extend(lista2)
    
    print(lista[-1])

    tupla = (3, 5, 7)
    
    print(tupla[0])

    inicio = int(input("Introduce el inicio: "))
    fin = int(input("Introduce el fin: "))
    salto = int(input("Introduce el salto: "))

    rango = range(inicio, fin, salto)
    print(rango)
    
if __name__ == "__main__":
    main()