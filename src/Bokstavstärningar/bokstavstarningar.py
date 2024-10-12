import sys; input = sys.stdin.readline
N, K, M = map(int, input().split()); F = {chr(x):set() for x in range(65, 91)}; Z = 0
for i in range(N):
    for f in input().strip(): F[f].add(1<<i)
def bt(w, idx=0, bm=0):
    if idx == N: return 1
    for p in F[w[idx]]:
        if bm&p == 0 and bt(w, idx+1, bm|p): return 1
    return 0
for _ in range(M): Z += bt(input().strip())
print(Z)