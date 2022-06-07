T=int(input())

for i in range(T):
    res=0
    N,K=map(int,input().split())
    snaps=[0 for x in range(N)]
    for j in range(K):
        for k in range(1,N):
            if snaps[:N-k]==[1 for x in range(N-k)]:
                if snaps[N-k]==0:
                    snaps[N-k]=1
                elif snaps[N-k]==1:
                    snaps[N-k]=0
        snaps[0]=1 if snaps[0]==0 else 0
    if snaps==[1 for x in range(N)]:
        res=1
    print("Case",'#'+str(i+1)+':',"OFF" if res==0 else "ON")

