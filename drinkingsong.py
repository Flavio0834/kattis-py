N=int(input())
mot=input()

for i in range(N):
    #print(N-i,"bottles of",mot,"on the wall,",N-i,"bottles of",mot+'.')
    #if i==N-1:
    #    x="no more bottles of milk."
    #else:
    #    x=str(N-i-1)+" bottle of milk on the wall.\n"
    #print("Take one down, pass it around,",x,)

    if i!=N-1 and i!=N-2:
        print(N-i,"bottles of",mot,"on the wall,",N-i,"bottles of",mot+'.')
        x=str(N-i-1)+" bottles of "+mot+" on the wall.\n"
        print("Take one down, pass it around,",x,)
    elif i==N-2:
        print(N-i,"bottles of",mot,"on the wall,",N-i,"bottles of",mot+'.')
        x=str(N-i-1)+" bottle of "+mot+" on the wall.\n"
        print("Take one down, pass it around,",x,)
    else:
        print(N-i,"bottle of",mot,"on the wall,",N-i,"bottle of",mot+'.')
        x="no more bottles of "+mot+'.'
        print("Take it down, pass it around,",x,)