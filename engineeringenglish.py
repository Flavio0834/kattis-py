words = set()
while True:
    try:
        a = input()
        res = ""
        for k in a.split():
            l = k.lower()
            if l not in words:
                words.add(l)
                res += k + " "
            else:
                res += ". "
        print(res.strip())

    except:
        break
