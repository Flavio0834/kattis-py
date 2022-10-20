L = [0, 0, 0, 0]
a = input()
while a != "":
    L[int(a) - 1] += 1
    a = input()
print(*L)
print(L.index(max(L)))
