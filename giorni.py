giorni="lunedì   martedì  mercoledìgiovedi  venerdì  sabato   domenica "
index=int(input("giorno"))
p=(index-1)*9
print(giorni[p:p+9])


formato="{:<-9s}"
print(formato % giorni[p])