
reddito=int(input("inserisci il reddito"))
aliquota=0.23
aliquota2=0.35
aliquota3=0.43
if reddito <= 28000:
    reddito*=aliquota
elif reddito<= 50000:
    reddito-=abs(28000)
    reddito*=aliquota2
    reddito+=6440
else :
    reddito-=abs(50000)
    reddito*=aliquota3
    reddito+=14140
print(reddito)