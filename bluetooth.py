n = int(input())

upper = ["n" for i in range(16)]
lower = ["n" for i in range(16)]

for i in range(n):
    tooth, type = input().split()
    if tooth[1] == "+":
        upper[8 - int(tooth[0])] = type
    elif tooth[0] == "+":
        upper[7 + int(tooth[1])] = type
    elif tooth[1] == "-":
        lower[8 - int(tooth[0])] = type
    elif tooth[0] == "-":
        lower[7 + int(tooth[1])] = type

if "b" in upper[:8] or "b" in lower[:8]:
    res = 0
    if "b" in upper[8:] or "b" in lower[8:]:
        res = 2
elif "b" in upper[8:] or "b" in lower[8:]:
    res = 1
    if "b" in upper[:8] or "b" in lower[:8]:
        res = 2

if res == 0:
    res = 2
    if "n" in upper[8:] and "n" in lower[8:]:
        res = 0
elif res == 1:
    res = 2
    if "n" in upper[:8] and "n" in lower[:8]:
        res = 1

print(res)
