import random
lista = ["Nacho","Vanesa","Tania","Andrea"]
posicion = random.randrange(len(lista))
def pato(lista, posicion):
    return(lista[posicion])

resultado = pato(lista,posicion)
print(resultado)
