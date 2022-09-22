while True:
    try:
        higher = []
        lower = []
        while True:
            a = int(input())
            b = input()
            if b == "too high":
                higher.append(a)
            elif b == "too low":
                lower.append(a)
            else:
                break
        dishonest = False
        for k in higher:
            if a >= k:
                dishonest = True
        for k in lower:
            if a <= k:
                dishonest = True
        print("Stan is dishonest" if dishonest else "Stan may be honest")

    except:
        break
