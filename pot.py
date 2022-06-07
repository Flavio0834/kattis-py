N=int(input())
res=0
for i in range(N):
    a=input()
    res+=(int(a[:len(a)-1])**int(a[len(a)-1]))
print(res)