"""
Pedir al usuario un número entero y mostrar por pantalla si el número es primo o no.
"""

numero = int(input("Número: "))

es_primo = True
limite = int(numero/2) + 1

if numero > 1:
    for i in range(2,limite):
        print(numero,"/",i)
        if numero % i == 0:
            es_primo = False
            break
else:
    es_primo = False
    
print(es_primo)

