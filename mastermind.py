line = input().split()
n = int(line[0])
a, b = list(line[1]), list(line[2])

r = 0
s = 0
for i in range(n):
    if a[i] == b[i]:
        r += 1
        a[i] = "x"
        b[i] = "y"

for i in range(n):
    if b[i] in a and i != a.index(b[i]):
        s += 1
        a[a.index(b[i])] = "x"

print(r, s)
