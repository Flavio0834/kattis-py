N = int(input())
for i in range(N):
    n = int(input())
    L = []
    for j in range(n):
        a, b, c = map(int, input().split())
        L.append((a, b, c))
    max = None
    index = 0
    for j in range(n):
        a, b, c = L[j]
        R = b / (2 * a)
        jmax = -a * R**2 + b * R + c
        if max == None or jmax > max:
            max = jmax
            index = j

    print(index + 1)
