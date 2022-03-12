import sys, math

def find(p, q):
    if p == 0:
        return 0, 2
    elif p == q:
        return 2, 2
    for n in range(2, 50001):
        if p*n*(n-1) % q != 0:
            continue
        k = p*n*(n-1) // q
        c = round(math.sqrt(1 + 4*k), 0)
        if abs(c**2 - (1 + 4*k)) < 1e-4 and n >= (1 + int(c)) // 2:
            return (1 + int(c)) // 2, n

for line in sys.stdin:
    p, q = map(int, line.split())
    if p + q == 0:
        break

    res = find(p, q)
    if not res:
        print('impossible')
    else:
        a, b = res
        print(a, b - a)