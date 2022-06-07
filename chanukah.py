P=int(input())
for i in range(P):
    k,n=map(int,input().split())
    print(k,round(((n+1)*(n+2)/2)-1))