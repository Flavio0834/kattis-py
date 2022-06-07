N=int(input())
for i in range(N):
    n=0
    k=int(input())
    for j in range(k):
        n+=1/2
        n*=2
    print(int(n))