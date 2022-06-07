T=int(input())

for i in range(T):
    poubelle=input()
    Ng,Nm=map(int,input().split())
    Lg=list(map(int,input().split()))
    Lm=list(map(int,input().split()))

    a=max(Lg)
    b=max(Lm)

    print("Godzilla" if a>=b else "MechaGodzilla")