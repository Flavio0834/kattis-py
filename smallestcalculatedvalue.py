a, b, c = map(int, input().split())

mini = float("inf")

if 0 <= a + b + c < mini:
    mini = a + b + c
if 0 <= a + b - c < mini:
    mini = a + b - c
if 0 <= (a + b) * c < mini:
    mini = (a + b) * c
if (a + b) % c == 0 and 0 <= (a + b) / c < mini:
    mini = (a + b) / c

if 0 <= a - b + c < mini:
    mini = a - b + c
if 0 <= a - b - c < mini:
    mini = a - b - c
if 0 <= (a - b) * c < mini:
    mini = (a - b) * c
if (a - b) % c == 0 and 0 <= (a - b) / c < mini:
    mini = (a - b) / c

if 0 <= a * b + c < mini:
    mini = a * b + c
if 0 <= a * b - c < mini:
    mini = a * b - c
if 0 <= a * b * c < mini:
    mini = a * b * c
if (a * b) % c == 0 and 0 <= a * b / c < mini:
    mini = a * b / c

if a % b == 0:
    if 0 <= a / b + c < mini:
        mini = a / b + c
    if 0 <= a / b - c < mini:
        mini = a / b - c
    if 0 <= a / b * c < mini:
        mini = a / b * c
    if (a / b) % c == 0 and 0 <= (a / b) / c < mini:
        mini = (a / b) / c

print(int(mini))
