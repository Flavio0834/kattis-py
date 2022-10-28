N = int(input())
L = [input()]
order = 3
for i in range(N - 1):
    L.append(input())
    if L[-1] > L[-2]:
        if order == 0:
            pass
        elif order == 1:
            order = 2
            break
        elif order == 3:
            order = 0
    elif L[-1] < L[-2]:
        if order == 1:
            pass
        elif order == 0:
            order = 2
            break
        elif order == 3:
            order = 1

if order == 2 or order == 3:
    print("NEITHER")
elif order == 0:
    print("INCREASING")
else:
    print("DECREASING")
