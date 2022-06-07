N=int(input())
for i in range(N):
    nb=int(input())
    liste=[]
    for j in range(nb):
        a=input()
        if a not in liste:
            liste.append(a)
    print(len(liste))