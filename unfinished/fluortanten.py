N=int(input())
L=list(map(int,input().split()))

if L[0]!=0:
    L.pop(L.index(0))
    M=[0]+L
else:
    M=L

hapmax=-9999999
for i in range(N):
    sum=0
    for j in range(N):
        sum+=(j+1)*M[j]
    if sum>hapmax:
        hapmax=sum
    if i!=N-1:
        M[i],M[i+1]=M[i+1],M[i]

print(hapmax)