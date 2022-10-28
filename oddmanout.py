N = int(input())
for i in range(N):
    G = int(input())
    L = list(map(int, input().split()))

    dico = dict()
    for k in L:
        if k in dico:
            dico[k] += 1
        else:
            dico[k] = 1

    for k in L:
        if dico[k] == 1:
            print("Case #{}: {}".format(i + 1, k))
            break
