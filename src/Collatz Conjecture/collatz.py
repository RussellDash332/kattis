table = {}

def f(n):
    return 3*n+1 if n%2 else n//2
    
def collatz_distance(n):
    if n == 1:
        return 0
    else:
        if n in table:
            return table[n]
        table[n] = collatz_distance(f(n))+1
        return table[n]

import sys
for line in sys.stdin:
    a,b = list(map(int,line.split(" ")))
    if a == 0 and b == 0:
        break

    c,d = a,b

    da, db = collatz_distance(a), collatz_distance(b)

    def do(c,d):
        for i in range(db+1):
            c = a
            for j in range(da+1):
                if c == d:
                    print(f'{a} needs {j} steps, {b} needs {i} steps, they meet at {d}')
                    return
                c = f(c)
            d = f(d)

    do(c,d)