n=int(input())
T=[]
D=[]
for i in range(n):
    t,d=map(int,input().split())
    T.append(t)
    D.append(d)

V=[]
for j in range(1,len(T)):
    V.append((D[j]-D[j-1])/(T[j]-T[j-1]))

print(int(max(V)))