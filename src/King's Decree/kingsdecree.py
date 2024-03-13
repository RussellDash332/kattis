import sys; input = sys.stdin.readline
def f(x):
    u = 0
    for i in q: u += max(0, x-i)
    return u <= t
for _ in range(int(input())):
    n = int(input()); s = sum(map(int, input().split())); q = [*map(int, input().split())]; t = s-sum(q); lo, hi = 0, 10**9
    while hi-lo>1:
        mi = (lo+hi)//2
        if f(mi): lo = mi
        else: hi = mi-1
    print(hi if f(hi) else hi-1)