import os

fileName =input("inserisci nome file") #"Massimo.txt"
if os.path.exists(fileName):
    
    file = open(fileName,"r")
    temp = file.readlines()
    Lines=[]

    for x in temp:
        Lines.append(float(x))

    numberMax = {}
    nTot = 0
    somma = 0
    for line in Lines:
        nTot += 1
        somma += line
        if line == max(Lines):
            numberMax[nTot]=line

    print(numberMax, somma/nTot)
else:
    name=os.getcwd()
    print("file non trovato: ", name)

