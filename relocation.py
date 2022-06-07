N,Q=map(int,input().split())
L=list(map(int,input().split()))
for i in range(Q):
    x=list(map(int,input().split()))
    if x[0]==1:
        L[x[1]-1]=x[2]
    else:
        print(abs(L[x[1]-1]-L[x[2]-1]))