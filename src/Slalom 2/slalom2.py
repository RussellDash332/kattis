import sys; input = sys.stdin.readline
w, vh, n = map(int, input().split())
xy = [[*map(int, input().split())] for _ in range(n)]
s = [int(input()) for _ in range(int(input()))]
s.append(-1e18), s.sort()

def f(k):
    lo, hi = -1e18, 1e18; py = 0
    for x, y in xy:
        lo, hi = max(x, lo-vh/k*(y-py)), min(x+w, hi+vh/k*(y-py)); py = y
        if lo > hi: return 0
    return 1

lo, hi = 0, len(s)-1
while hi-lo>1:
    mi = (lo+hi)//2
    if f(s[mi]): lo = mi
    else: hi = mi-1
ans = s[hi] if f(s[hi]) else s[hi-1]
if ans == s[0]: print('IMPOSSIBLE')
else: print(ans)