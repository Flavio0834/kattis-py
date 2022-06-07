L=list(map(int,input().split()))
res=1
for i in range(len(L)):
    res=res*L[i]
print(res)