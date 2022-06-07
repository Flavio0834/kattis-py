x=input()
L=[1,0,0]
for k in x:
    if k=='A':
        L[0],L[1]=L[1],L[0]
    elif k=='B':
        L[1],L[2]=L[2],L[1]
    else:
        L[0],L[2]=L[2],L[0]

print(L.index(1)+1)