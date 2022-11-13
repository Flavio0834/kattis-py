a = input()

T = a.count("T")
C = a.count("C")
G = a.count("G")

score = T**2 + C**2 + G**2

while T and C and G:
    score += 7
    T -= 1
    C -= 1
    G -= 1

print(score)
