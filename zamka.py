L=int(input())
D=int(input())
X=int(input())

N=L
while sum(int(x) for x in str(N))!=X:
    N+=1

M=D
while sum(int(x) for x in str(M))!=X:
    M-=1

print(N)
print(M)