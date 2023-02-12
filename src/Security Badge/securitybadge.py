import sys
sys.setrecursionlimit(1010)
N, L, B = map(int, input().split())
S, D = map(int, input().split())

g = [{} for _ in range(N)]
pts = set()
for line in sys.stdin:
    a, b, x, y = map(int, line.split())
    g[a-1][b-1] = (x, y)
    pts.add(x)
    pts.add(y+1)

pts = sorted(pts)
def dfs(u, pt, vis=1):
    if vis == 1: vis = set()
    if u == D: return True
    if u in vis: return False
    vis.add(u)
    for v, (s, e) in g[u].items():
        if s <= pt <= e and dfs(v, pt, vis): return True
    return False

S, D = S-1, D-1
# if dfs on pts[i] is True, everything in [pts[i], pts[i+1]) works
print(sum(pts[i+1]-pts[i] for i in range(len(pts)-1) if dfs(S, pts[i])))