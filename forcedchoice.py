N,P,S=map(int,input().split())
for i in range(S):
    L=list(map(int,input().split()))
    print('KEEP' if P in L[1:] else 'REMOVE')