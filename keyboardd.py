s = input()
t = input()

j = 1
L = []
for i in range(1, len(s)):
    if t[j] == t[j - 1] and t[j] != s[i]:
        if t[j] not in L:
            L.append(t[j])
        j += 1
    j += 1
if t[-1] not in L and t[-1] == t[-2]:
    L.append(t[-1])
print("".join(L))
# Works on samples but not when submitting.
# https://open.kattis.com/problems/keyboardd
