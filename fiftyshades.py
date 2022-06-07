N=int(input())

somme=0
for i in range(N):
    mot=input().lower()
    if (("rose" in mot) or ("pink" in mot)):
        somme+=1

if somme>0:
    print(somme)
else:
    print("I must watch Star Wars with my daughter")