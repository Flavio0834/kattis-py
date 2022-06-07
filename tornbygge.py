N=int(input())
A=list(map(int,input().split()))

tours=1
for i in range(1,N):
    if A[i-1]<A[i]:
        tours+=1

print(tours)