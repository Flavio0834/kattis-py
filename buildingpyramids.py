N = int(input())
floors = 0
i = 1
while N > 0:
    if N - i**2 >= 0:
        N -= i**2
        i += 2
        floors += 1
    else:
        break
print(floors)
