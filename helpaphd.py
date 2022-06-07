N=int(input())
for i in range(N):
    x=input()
    if x=="P=NP":
        print('skipped')
    else:
        a,b=map(int,x.split('+'))
        print(a+b)