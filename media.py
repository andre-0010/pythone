#acquisire tramite input() una sequenza di valori numerici fihno a che l'utente non scriva exit, esegire la media dei valori letti
stringa=""
media=0
contatore=0
while True:
    stringa=input("inserisci un numero: ").lower()
    if stringa=="exit" :
        break
    contatore+=1
    media+=int(stringa)
media/=contatore
print("La media è:", media)