V = int(input())
price_min = V * 4 + 2
good_i = 0
for i in range(2, V):
    if V % i != 0:
        continue
    price = 2 * (V // i) * i + 2 * i + 2 * (V // i)
    if price < price_min:
        price_min = price
        good_i = i
if good_i:
    price_min_old = price_min
    for i in range(2, good_i):
        if good_i % i != 0:
            continue
        price = (
            2 * (V // good_i) * (good_i // i)
            + 2 * (good_i // i) * i
            + 2 * (V // good_i) * i
        )
        if price < price_min:
            price_min = price
if good_i and price_min == price_min_old:
    price_min_old = price_min
    for i in range(2, (V // good_i)):
        if (V // good_i) % i != 0:
            continue
        price = (
            2 * ((V // good_i) // i) * good_i
            + 2 * good_i * i
            + 2 * ((V // good_i) // i) * i
        )
        if price < price_min:
            price_min = price
if good_i:
    price_min_old = price_min
    for i in range(2, good_i):
        if good_i % i != 0:
            continue
        price = (
            2 * (V // good_i) * (good_i // i)
            + 2 * (good_i // i) * i
            + 2 * (V // good_i) * i
        )
        if price < price_min:
            price_min = price

print(price_min)
