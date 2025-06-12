import sys

input()
def f(a, b, c):
    return a**2 + b**2 + c**2 + 7*min(a,b,c)

for line in sys.stdin:
    a, b, c, d = map(int, line.split())
    best = 0
    if min(a, b, c) < 10 and d < 25:
        for d1 in range(d+1):
            for d2 in range(d+1-d1): best = max(best, f(a+d1, b+d2, c+d-d1-d2))
    else:
        best = max(f(a+d, b, c), f(a, b+d, c), f(a, b, c+d))
    print(best)