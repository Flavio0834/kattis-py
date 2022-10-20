N = input()
M = input()

if M == "1":
    print(N)
else:
    zeros = M.count("0")

    first = N[0]
    if first == "0":
        N = N[1:]
        first = N[0]

    if len(N) >= zeros:
        res = N[::-1]
        res = res[:zeros] + "." + res[zeros:]
        res = res[::-1]
    else:
        res = N[::-1]
        res = res + "0" * (zeros - len(N)) + "."
        res = res[::-1]

    last = res[-1]
    while last == "0":
        res = res[:-1]
        last = res[-1]

    first = res[0]
    while first == "0":
        res = res[1:]
        first = res[0]

    if res[0] == ".":
        res = "0" + res

    if res[-1] == ".":
        res = res[:-1]

    print(res)
