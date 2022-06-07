N,M=map(int,input().split())
L=[]
for i in range(N+M):
    L.append(0)

for i in range(N):
    for j in range(M):
        L[i+j]+=1

x=max(L)
for i in range(len(L)):
    if L[i]==x:
        print(i+2)