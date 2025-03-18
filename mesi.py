#scrivere un progrfamma per tradurre i numeri da 1 a 12 nei nomi dei mesi corrispondenti


numero=int(input("numero del mese"))
mesi="Gennaio  Febbraio Marzo    Aprile   Maggio   Giugno   Luglio   Agosto   SettembreOttobre  Novembre Dicembre"
p=(numero-1)*9

#print(mesi[((numero-1)*9)]+mesi[(numero-1)*9+1]+mesi[(numero-1)*9+2]+mesi[(numero-1)*9+3]+mesi[(numero-1)*9+4]+mesi[(numero-1)*9+5]+mesi[(numero-1)*9+6]+mesi[(numero-1)*9+7]+mesi[(numero-1)*9+8])
print(mesi[p:p+9])
