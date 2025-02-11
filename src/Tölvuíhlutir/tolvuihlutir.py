import sys; input = sys.stdin.readline
n, k, p = map(int, input().split())
m = {e:i for i,e in enumerate(input().strip().split())}
v = [[] for _ in range(k)]; lo, hi = 0, 10**9
for _ in range(n): c, x, q = input().split(); v[m[c]].append((int(x), int(q)))
def f(n):
    s = 0
    for w in v:
        s += min((a for a,b in w if b >= n), default=p+1)
        if s > p: return 0
    return 1
while hi-lo>1:
    if f(mi:=(lo+hi)//2): lo = mi
    else: hi = mi-1
print(ans if f(ans:=hi if f(hi) else hi-1) else 'O nei!')