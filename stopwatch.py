N=int(input())
if N%2==1:
    print("still running")
else:
    res=0
    etat=False
    L=[]
    for i in range(N):
        L.append(int(input()))
    for i in range(0,L[-1]+1):
        if etat==True:
            res+=1
        if i in L:
            etat=not etat
    print(res)