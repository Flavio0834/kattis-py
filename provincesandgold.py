G,S,C=map(int,input().split())
bp=3*G+2*S+1*C
okvic=''
oktre=''
if bp>=2 and bp<5:
    okvic="Estate"
elif bp>=5 and bp<8:
    okvic="Duchy"
elif bp>=8:
    okvic="Province"

if bp>=0 and bp<3:
    oktre="Copper"
elif bp>=3 and bp<6:
    oktre="Silver"
elif bp>=6:
    oktre="Gold"

if oktre=='':
    print(okvic)
elif okvic=='':
    print(oktre)
else:
    print(okvic,'or',oktre)