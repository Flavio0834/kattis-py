# Créé par ordis, le 22/09/2021 en Python 3.7


n=int(input())
liste=[]



def quicksort(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        t1 = []
        t2 = []
        for x in t[1:]:
            if x<pivot:
                t1.append(x)
            else:
                t2.append(x)
    return quicksort(t1)+[pivot]+quicksort(t2)



for i in range(n):
    a,b,c,d,e=map(int,input().split())
    liste.append(quicksort([a,b,c,d,e]))

liste2=[]
for i in range(len(liste)):
    liste2.append(0)

for i in range(len(liste)):
    for m in liste:
        if liste[i]==m:
            liste2[i]+=1

maxi=max(liste2)

res=0
for i in range(len(liste2)):
    if liste2[i]==maxi:
        res+=1
print(res)
