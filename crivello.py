n=100
lista={x for x in range(2,n+1)}

for x in range(2,n+1):
    for y in range(2,int(x**0.5)+1):
        if x%y == 0:
            try:
                lista.discard(x)
            except:
                print("errore","y:",y,"x:",x)

print(lista, len(lista))


# n=100
# lista=[x for x in range(2,n+1)]

# for x in lista:
#     for y in range(2,int(x**0.5)+1):
#         if y%x != 0:
#             try:
#                 lista.remove(y)
#                 break
#             except:
#                 print("y:",y,"x:",x)

# print(lista, len(lista))









