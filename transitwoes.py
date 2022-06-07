s,t,n=map(int,input().split())
D=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

s+=D[0]
for i in range(1,n+1):
    s+=C[i-1]-(s%C[i-1]) if s<C[i-1] else s%C[i-1]
    s+=B[i-1]
    s+=D[i]

print("yes" if s<=t else 'no')