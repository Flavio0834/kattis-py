T=int(input())

for i in range(T):
    poubelle=input()
    Ng,Nm=map(int,input().split())
    Lg=list(map(int,input().split()))
    Lm=list(map(int,input().split()))

    while Lg!=[] and Lm!=[]:
        if min(min(Lg),min(Lm))==min(Lm) or min(Lg)==min(Lm):
            Lm.pop(Lm.index(min(Lm)))
        elif min(min(Lg),min(Lm))==min(Lg):
            Lg.pop(Lg.index(min(Lg)))

    print("Godzilla" if Lm==[] else "MechaGodzilla")