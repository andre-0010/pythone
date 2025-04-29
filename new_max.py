import os

fileName =input("inserisci nome file")
if os.path.exists(fileName):
    with open(fileName, "r") as file:
       Lines = [float(line.strip()) for line in file.readlines()]
    
    massimo = max(Lines)
    MaxValuesIndex = [index for index, value in enumerate(Lines) if value==massimo]
    print(f"Numero Massimo: {massimo} in posizione: {MaxValuesIndex}| Media: {sum(Lines)/len(Lines)}") 
    

    #Lines=enumerate(Lines)
    #print(list(Lines))
    #Lines=[Lines if Lines.values==max()]

    #numberMax = {}
    #nTot = 0
    #somma = 0
    
    # for line in Lines:
    #     nTot += 1
    #     somma += line #line.get()
    #     if line == max(Lines): # if!=Lines.values()
    #         numberMax[nTot]=line #del Lines[nTot]
    
    #print("Numeri massimi: ", numberMax, "media: ", somma/nTot)

else:
    name=os.getcwd()
    print(f"file {fileName} non trovato in: ", name)

