T=int(input())
for i in range(T):
    L=list(map(int,input().split()))
    res=0
    for j in range(1,len(L)):
        if L[j]>2*L[j-1] and L[j]!=0:
            res+=L[j]-(2*L[j-1])
    print(res)
