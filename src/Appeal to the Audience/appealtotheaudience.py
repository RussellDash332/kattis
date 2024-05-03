import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**5)
n, k = map(int, input().split())
a = sorted(map(int, input().split()))
p = [int(input()) for _ in range(n-1)]
g = [[] for _ in range(n)]
for i in range(n-1): g[p[i]].append(i+1)

D = []
def trav(v, d):
    if not g[v]: return 1
    m = []
    for u in g[v]: m.append(trav(u, d+1))
    k = max(m)
    for i in range(len(m)):
        if k == m[i]:
            for j in range(len(m)):
                if i != j: D.append(m[j])
            return k+1
D.append(trav(0, 0)); t = sorted(D); t[-1] -= 1; print(sum(x*y for x, y in zip(t, a)))