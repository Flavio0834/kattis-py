N=int(input())
A=[]

for i in range(N):
    A.append(int(input()))

n=[]
for i in range(A[len(A)-1]):
    n.append(i+1)

k=set(n)-set(A)
if k==set():
    print("good job")
else:
    k=sorted(k)
    for i in k:
        print(i)
