saluto="Ci vediamo puntuali domani mattina"
lista= list(saluto)
insieme=set(lista)
occorrenze = {}
mytuple = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}


def conta(stringa):
    for lettera in insieme:
        occorrenze[lettera]=saluto.count(lettera)
    print(occorrenze)
    for x in occorrenze:
        if occorrenze.get(x) == max(occorrenze.values()):
            print(x, occorrenze[x])
    print(mytuple.difference(insieme))

conta(saluto)