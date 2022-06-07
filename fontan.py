# Façon brutale

# Récup input
N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(input())

Lorigin=[]
while L!=Lorigin:
    Lorigin=L.copy()
    Linterdite=[]
    for i in range(N):
        for j in range(M):
            if L[i][j]=='V' and (i,j) not in Linterdite:
                if i+1<N:
                    if L[i+1][j]=='.':
                        L[i+1]=L[i+1][:j]+'V'+L[i+1][j+1:]
                        Linterdite.append((i+1,j))
                    elif L[i+1][j]=='#':
                        if j-1>=0 and L[i][j-1]=='.':
                            L[i]=L[i][:j-1]+'V'+L[i][j:]
                            Linterdite.append((i,j-1))
                        if j+1<M and L[i][j+1]=='.':
                            L[i]=L[i][:j+1]+'V'+L[i][j+2:]
                            Linterdite.append((i,j+1))

for k in L:
    print(k)