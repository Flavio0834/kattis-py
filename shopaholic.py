N=int(input())
L=list(map(int,input().split()))
L.sort()
L.reverse()
res=0
for i in range(len(L)):
    if (i+1)%3==0:
        res+=L[i]
print(res)