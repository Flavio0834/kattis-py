x=int(input())
n=int(input())
reste=0
for i in range(n):
    mois=int(input())
    if mois<x:
        reste+=x-mois
    else:
        reste-=mois-x
print(x+reste)