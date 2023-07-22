import sys
for l in sys.stdin:
    n, p = int(l), 35
    if n == 0: break
    while p:
        if round(abs(n)**(1/p))**p == abs(n): print(p); break
        p -= 1+(n<0)