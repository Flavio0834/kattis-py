X,Y,N=map(int,input().split())
L=[x+1 for x in range(N)]
for i in range(len(L)):
    if L[i]%X==0 and L[i]%Y==0:
        L[i]='FizzBuzz'
    elif L[i]%X==0:
        L[i]='Fizz'
    elif L[i]%Y==0:
        L[i]='Buzz'

for k in L:
    print(k)