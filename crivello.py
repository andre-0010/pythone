n=100
lista=[x for x in range(2,n+1)]

for x in range(2, n+1):
    for y in range(2,int(x**0.5)+1):
        if x%y == 0:
            try:
                lista.remove(x)
            except:
                print("errore ",y)

print(lista, len(lista))









