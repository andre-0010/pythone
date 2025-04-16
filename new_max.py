import os

fileName =input("inserisci nome file")
if os.path.exists(fileName):
    
    file = open(fileName,"r")
    temp = file.readlines()
    Lines=[]

    for x in temp:
        Lines.append(float(x))



    numberMax = {}
    nTot = -1
    somma = 0
    for line in Lines:
        nTot += 1
        somma += line
        if line == max(Lines):
            numberMax[nTot]=line

    print("Numeri massimi: ", numberMax, "media: ", somma/nTot)
else:
    name=os.getcwd()
    print("file non trovato: ", name)

