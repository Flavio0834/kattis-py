N=int(input())
for i in range(N):
    A=list(map(int,input().split()))
    res=1
    for j in range(1,len(A)):
        res+=(A[j]-1)
    print(res)
