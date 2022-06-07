x=input()
y=int(x)
while y%(sum(int(k) for k in x))!=0:
    y+=1
    x=str(y)
print(y)