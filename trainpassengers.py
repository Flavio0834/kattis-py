possible = True
C, n = map(int, input().split())
people = 0
for i in range(n):
    left, entered, stayed = map(int, input().split())
    if left > people:
        possible = False
        break
    people += entered - left
    if people > C:
        possible = False
        break
    if people < 0:
        possible = False
        break
    if stayed != 0 and people != C:
        possible = False
        break
if people != 0:
    possible = False
print("possible" if possible else "impossible")
