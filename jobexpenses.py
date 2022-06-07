N=int(input())
L=list(map(int,input().split()))
res=0
for k in L:
    if k<0:
        res+=-k
        
print(res)