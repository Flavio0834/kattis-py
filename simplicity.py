word = input()

letters = dict()

for k in word:
    if k not in letters.keys():
        letters[k] = 1
    else:
        letters[k] += 1

a = len(letters.keys())
b = sorted(list(letters.values()))

res = 0
while a > 2:
    res += b.pop(0)
    a -= 1

print(res)
