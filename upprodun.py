N=int(input())
M=int(input())

r=M%N
n=N
while n!=0:
    if r!=0:
        print('*'*((M//N)+1))
        r-=1
    else:
        print('*'*(M//N))
    n-=1