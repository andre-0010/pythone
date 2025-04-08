saluto="Ci vediamo puntuali domani mattina"
occorrenze = {}


def conta(stringa):
    mytuple = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    lista= list(stringa)
    insieme=set(lista)
    massimi = {}
    for lettera in insieme:
        occorrenze[lettera]=stringa.count(lettera)
    for x in occorrenze:
        if occorrenze.get(x) == max(occorrenze.values()):
            #print(x, occorrenze[x])
            massimi[x]=occorrenze[x]
    #print(mytuple.difference(insieme))
    return occorrenze, massimi, mytuple.difference(insieme)
print(conta(saluto))