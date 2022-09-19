n = int(input())
e, kfact = 1, 1
for i in range(1, n + 1):
    e += 1 / kfact
    kfact *= i + 1

print(e)
