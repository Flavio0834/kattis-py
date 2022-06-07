N=int(input())
A=set(map(int,input().split()))
B=set(map(int,input().split()))
print(list(A-B)[0])