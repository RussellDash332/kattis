import sys; input = sys.stdin.readline
N, M = map(int, input().split()); G = [[] for _ in range(N)]
for _ in range(M): a, b, w = map(int, input().split()); G[a-1] += [(b-1, -w)]
def f(x):
    D = [10**18]*N; D[0] = 0
    for a in range(N):
        for b, w in G[a]: D[b] = min(D[b], D[a]+w+x)
    return D[-1]<=0
lo = 0; hi = 2e6
while abs(lo-hi)>1e-6:
    mi = (lo+hi)/2
    if f(mi): lo = mi
    else: hi = mi
print(lo)