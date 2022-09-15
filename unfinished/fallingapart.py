n=int(input())
L=list(map(int,input().split()))
print(sum(sorted(L)[::-2]),sum(sorted(L)[1::-2]))