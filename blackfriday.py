n=int(input())
A=list(map(int,input().split()))
B=[]
for i in range(6):
    B.append(0)
for k in A:
    B[k-1]+=1

occ=0
x=[]
for i in range(len(B)):
    if B[i]==1:
        occ+=1
        x.append(i+1)
x.sort()

if x==[]:
    print("none")
else:
    print(A.index(x[-1])+1)