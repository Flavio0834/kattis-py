L=list(map(int,input().split()))
M=[1,1,2,2,2,8]
for i in range(6):
    M[i]-=L[i]
print(*M)