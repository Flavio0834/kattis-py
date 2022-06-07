A,B=input().split()

x=True
i=-1
while x:
    i+=1
    if A[i] in B:
        x=False
        X=A[i]

L=[]
for b in range(len(B)):
    ligne=''
    for a in range(len(A)):
        ligne+='.'
    L.append(ligne)

L[B.index(X)]=A
for b in range(len(B)):
    if b!=B.index(X):
        ligne=''
        for m in range(len(L[b])):
            if m!=i:
                ligne+='.'
            else:
                ligne+=B[b]
        L[b]=ligne

for z in L:
    print(z)
