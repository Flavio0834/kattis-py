def update(index,val,arbre):
    while index<len(arbre):
        arbre[index]+=val
        index+=index&-index

def somme(index,arbre):
    res=0
    while index>0:
        res+=arbre[index]
        index-=index&-index
    return res

N,n=map(int,input().split())
L=[]
for i in range(N):
    L.append(0)

for i in range(n):
    X=list(input().split())
    if X[0]=='+':
        index,val=map(int,(X[1],X[2]))
        update(index,val,L)
    else:
        index=int(X[-1])
        print(somme(index,L))