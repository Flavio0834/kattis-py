N=int(input())
for i in range(N):
    a,b,c=map(int,input().split())
    print("Possible" if a+b==c or a-b==c or b-a==c or a*b==c or a/b==c or b/a==c else "Impossible")