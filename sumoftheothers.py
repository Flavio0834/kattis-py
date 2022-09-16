while True:
    try:
        L = list(map(int, input().split()))
        for i in range(len(L)):
            if sum(L[:i] + L[i + 1 :]) == L[i]:
                break
        print(L[i])
    except:
        break
