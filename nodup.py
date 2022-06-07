L=list(input().split())
liste=[]
res=1
for k in L:
    if k not in liste:
        liste.append(k)
    else:
        res=0

print('yes' if res==1 else 'no')