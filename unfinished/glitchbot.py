def check(instruction):
    global angle
    global x
    global y
    global xf
    global yf
    global deltas
    if instruction == "Left":
        # Test if it was a good idea to turn left
        if (
            (deltas[(angle - 1) % 4][0] < 0 and xf >= x)
            or (deltas[(angle - 1) % 4][0] > 0 and xf <= x)
            or (deltas[(angle - 1) % 4][1] < 0 and yf >= y)
            or (deltas[(angle - 1) % 4][1] > 0 and yf <= y)
        ):
            return False
    elif instruction == "Right":
        if (
            (deltas[(angle + 1) % 4][0] < 0 and xf >= x)
            or (deltas[(angle + 1) % 4][0] > 0 and xf <= x)
            or (deltas[(angle + 1) % 4][1] < 0 and yf >= y)
            or (deltas[(angle + 1) % 4][1] > 0 and yf <= y)
        ):
            return False
    else:
        # instruction is Forward
        if (
            ((xf - (x + deltas[angle][0])) > xf - x)
            or ((yf - (y + deltas[angle][1])) > yf - y)
            or (deltas[angle][0] != 0 and xf == x)
            or (deltas[angle][1] != 0 and yf == y)
        ):
            return False
    return True


xf, yf = map(int, input().split())
n = int(input())
x, y = 0, 0
angle = 0
for i in range(n):
    instruction = input()
    # angle = 0/1(90)/2(180)/3(270)
    # Left/Right angle = angle+-1%4
    deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    good = check(instruction)
    print(instruction, x, y, xf, yf, angle, good)
    if good:
        if instruction == "Left":
            angle = (angle - 1) % 4
        elif instruction == "Right":
            angle = (angle + 1) % 4
        else:
            x, y = x + deltas[angle][0], y + deltas[angle][1]
    else:
        if (xf - (x + 1) < xf - x) or (yf - (y + 1) < yf - y):
            print(i + 1, "Forward")
        #  now test if it is pertinent to turn Left
        elif check("Left"):
            print(i + 1, "Left")
        else:
            print(i + 1, "Right")
        break
    print(instruction, x, y, xf, yf, angle, good)
