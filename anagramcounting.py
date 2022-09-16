import math

while True:
    try:
        a = input()
        res = math.factorial(len(a))
        ens = dict()
        for k in a:
            if k not in ens:
                ens[k] = 1
            else:
                ens[k] += 1
        for k in ens:
            res //= math.factorial(ens[k])
        print(int(res))
    except:
        break
