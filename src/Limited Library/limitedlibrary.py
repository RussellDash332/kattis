import sys; input = sys.stdin.readline
n, m, x, y = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
def f(k):
    p1 = p2 = 0; c = [y]*k+[x]*(n-k)
    while p1 < n and p2 < m:
        if a[p1] < b[p2] or c[p1] == 0: p1 += 1
        else: c[p1] -= 1; p2 += 1
    return p2 == m
lo, hi = 0, n
while hi-lo>1:
    if f(mi:=(lo+hi)//2): lo = mi
    else: hi = mi-1
ans = hi if f(hi) else hi-1
print(ans if f(ans) else 'impossible')