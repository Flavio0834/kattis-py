T=int(input())
for i in range(T):
    a=input()
    L=list(map(int,input().split()))
    print((max(L)-min(L))*2)