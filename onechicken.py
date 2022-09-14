N, M = map(int, input().split())

if N - M == -1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
elif N - M == 1:
    print("Dr. Chaz needs 1 more piece of chicken!")
else:
    if N - M <= 0:
        print("Dr. Chaz will have " + str(abs(N - M)) + " pieces of chicken left over!")
    else:
        print("Dr. Chaz needs " + str(N - M) + " more pieces of chicken!")
