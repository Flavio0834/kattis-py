N=int(input())
L=list(map(int,input().split()))
M=[]
for i in range(N):
    if L[i]!=-1:
        M.append(L[i])
print(sum(M)/len(M))