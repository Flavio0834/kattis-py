from math import factorial, log2

m, n, t = map(int, input().split())
operations = [
    lambda x: factorial(n),
    lambda x: 2**x,
    lambda x: x**4,
    lambda x: x**3,
    lambda x: x**2,
    lambda x: x * log2(x),
    lambda x: x,
]

print("AC" if operations[t - 1](n) <= m else "TLE")
