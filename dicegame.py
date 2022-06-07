# Créé par ordis, le 04/10/2021 en Python 3.7

a1,b1,a2,b2=map(int,input().split())
c1,d1,c2,d2=map(int,input().split())


esp1=0
k=0
for i in range(a1,b1+1):
    for j in range(a2,b2+1):
        esp1+=i+j
        k+=1
esp1/=k

esp2=0
k=0
for i in range(c1,d1+1):
    for j in range(c2,d2+1):
        esp2+=i+j
        k+=1
esp2/=k

print("Emma" if esp2>esp1 else "Tie" if esp2==esp1 else "Gunnar")
