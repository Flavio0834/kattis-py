N,M,A,B=map(int,input().split())
L=[]
for i in range(N):
    L.append(input())

total=0
hauts=0
for i in range(N):
    for j in range(M):
        if L[i][j]=='#':
            hauts+=1
            prix=0
            if i-1>=0 and L[i-1][j]=='.':
                prix+=1000
            if i+1<N and L[i+1][j]=='.':
                prix+=1000
            if j-1>=0 and L[i][j-1]=='.':
                prix+=1000
            if j+1<M and L[i][j+1]=='.':
                prix+=1000

            if prix>=2000:
                total+=2000
            else:
                total+=prix

if total>=hauts*2000:
    if hauts<=N*M-hauts:
        print(hauts*2000)
    else:
        print((N*M-hauts)*2000)
else:
    print(total)