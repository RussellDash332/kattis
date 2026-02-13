import sys; input = sys.stdin.readline
N = int(input()); P = sorted([*map(int, input().split())] for _ in range(N))
def f(x):
    r = 0
    for d, c in P:
        if x+c-r > d: return 1
        r += d-x-c; x = d+1
    return 0
lo, hi = 0, 10**9
while lo < hi:
    if f(mi:=(lo+hi)//2): hi = mi
    else: lo = mi+1
print(lo-1 if lo else 'impossible')