lista=list()
for x in range(1,11):
    lista.append(1/x)
formato="%2.8f"
for x in lista:
    print(formato % x)

