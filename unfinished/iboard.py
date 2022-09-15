while True:
    try:
        a = input()
        # convert phrase into ascii binary using encode
        b = a.encode()
        b = int.from_bytes(b, "big")
        b = bin(b)

        print(b)
        print(
            "free" if (b.count("1") % 2 == 0 and b.count("0") % 2 == 0) else "trapped"
        )
        print(b.count("1"), b.count("0"))
    except:
        break
