n = int(input())
while n:
    beacons = []
    for i in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    xmin, xmax = beacons[0][0], beacons[0][0]
    ymin, ymax = beacons[1][1], beacons[1][1]
    ixmin, ixmax, iymin, iymax = 0, 0, 0, 0
    for i in range(len(beacons)):
        x, y = beacons[i][0], beacons[i][1]
        if x < xmin:
            xmin = x
            ixmin = i
        if x > xmax:
            xmax = x
            ixmax = i
        if y < ymin:
            ymin = y
            iymin = i
        if y > ymax:
            ymax = y
            iymax = i
    print(xmin, xmax, ymin, ymax)
    print((xmax - xmin) * (ymax - ymin))
    n = int(input())
    # The robot can only go straight to a beacon, so the area won't always be a rectangle.
