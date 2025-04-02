# ES P5.22 PAG 334
#SCRIVETE UNA funzione che calcoli il saldo di un conto bancario dopo che siano trascorsi un dato numero di anni, 
# a partire da un dato saldo iniziale, e con un dato tasso di interesse annuo, accreditando gli interessi annualmente
def saldo(saldo_iniziale , numero_anni=None, tasso=0.1) :
    i=0
    saldo_attuale=saldo_iniziale
    if numero_anni==None:
        while i<20:
            saldo_attuale=(saldo_attuale*tasso)+saldo_attuale
            print("anno ",i+1,"° saldo:",saldo_attuale)
            i+=1
        return ""
    else:
        while i < numero_anni:
            saldo_attuale=(saldo_attuale*tasso)+saldo_attuale
            i+=1
        return saldo_attuale
  

        

# i=0
#         saldo_attuale=saldo_iniziale
#         while i<numero_anni:
#             saldo_attuale=(saldo_attuale*tasso)+saldo_attuale
#             print("anno ",i+1,"° saldo:",saldo_attuale)
#             i+=1
def main():
    saldo_iniziale=10000.0
    numero_anni=None
    tasso=0.01
    print(saldo(saldo_iniziale, numero_anni, tasso))





main()