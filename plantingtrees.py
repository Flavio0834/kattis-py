N=int(input())
A=sorted(list(map(int,input().split())))[::-1]
B=[]
t=1
for k in A:
    t+=1
    B.append(k+t)

print(max(B))