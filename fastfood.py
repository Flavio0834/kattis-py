N=int(input())
for i in range(N):
    prix=0
    n,m=map(int,input().split())
    A=[]
    for j in range(n):
        A.append(list(map(int,input().split())))
    B=list(map(int,input().split()))
    for L in A:
        mini=B[L[1]-1]
        for i in range(1,L[0]):
            if B[L[i+1]-1]<mini:
                mini=B[L[i+1]-1]
        prix+=mini*L[-1]
    print(prix)