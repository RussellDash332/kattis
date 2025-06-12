import sys; input = sys.stdin.readline
n, m = map(int, input().split()); R = {}; D = [set() for _ in range(m)]; L = set(); Z = set(); Q = []; S = set()
for i in range(m):
    ni, mi = map(int, input().split()); Q.append(ni)
    for _ in range(mi): p = input().strip(); R[p] = i
for _ in range(int(input())):
    p = input().strip()
    if p in S:
        S.discard(p)
        if p in R: D[R[p]].discard(p)
    elif p in L:
        L.discard(p)
        if p in R: D[R[p]].discard(p)
    else:
        L.add(p)
        if len(L) > n: L.discard(p); S.add(p); Z.add(p) # free spot
        elif p not in R: Z.add(p) # registered
        elif len(D[R[p]]) >= Q[R[p]]: D[R[p]].add(p); Z.add(p) # quota
        else: D[R[p]].add(p)
print(len(Z))
for i in sorted(Z): print(i)