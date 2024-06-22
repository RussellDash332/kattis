import sys; input = sys.stdin.readline; from math import gcd
W, N = map(int, input().split()); H = set(); M = set()
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    A = y2-y1; B = x1-x2; C = A*x1+B*y1; D = gcd(A, B, C); A //= D; B //= D; C //= D
    if A < 0: A, B, C = -A, -B, -C
    elif A == 0 and B < 0: B, C = -B, -C
    elif A == B == 0: C = abs(C)
    H.add((A, B, C))
for a, b, _ in H:
    d = gcd(a, b); a //= d; b //= d
    if a < 0: a, b = -a, -b
    elif a == 0: b = abs(b)
    M.add((a, b))
if len(M) == 1: w = len(H)+1
else: w = 2*len(H)
if w >= W: print(0)
else: print(max(1, (W+1)//2-len(H)))