r,n=map(int,input().split())
k=0
L=[]
if n==r:
    print("too late")
else:
    for i in range(n):
        L.append(int(input()))
    for i in range(1,r+1):
        if i not in L:
            print(i)
            break