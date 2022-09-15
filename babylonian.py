N = int(input())
for i in range(N):
    number = input()
    b = number.split(",")
    res = 0
    k = 0
    for j in range(len(b)):
        if b[len(b) - j - 1] != "":
            b[len(b) - j - 1] = int(b[len(b) - j - 1])
            res += b[len(b) - j - 1] * (60**j)
    print(res)
