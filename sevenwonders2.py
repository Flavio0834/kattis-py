a = input()

T = a.count("T")
C = a.count("C")
G = a.count("G")

score = T**2 + C**2 + G**2

if T > 0 and C > 0 and G > 0:
    score += 7

print(T, C, G, score)
