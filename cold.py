N=int(input())
L=list(map(int,input().split()))
res=0
for i in range(N):
    if L[i]<0:
        res+=1
print(res)