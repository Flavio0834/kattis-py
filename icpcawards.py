N=int(input())
L=[]
for i in range(N):
    x=list(input().split())
    ind=0
    for k in L:
        if x[0] in k:
            ind=1
    if ind==0 and len(L)<12:
        L.append(x)

for k in L:
    print(*k)