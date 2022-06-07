N=int(input())
L=[]
for i in range(N):
    L.append(input())

k=L[0]
cpt=0
for i in range(1,len(L)):
    if L[i]==k:
        cpt+=1
    k=L[i]

print(cpt)