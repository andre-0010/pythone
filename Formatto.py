lista=set()
for x in range(1,11):
    lista.add(1/x)
formato="%2.8f"
for x in lista:
    print(formato % x)

