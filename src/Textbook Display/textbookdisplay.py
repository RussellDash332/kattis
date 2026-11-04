N, *A = map(int, open(0).read().split())
P = []
for p in range(2, min(int(N**.5)+1, N)):
    for i in range(2, int(p**.5)+1):
        if p%i<1: break
    else: P += [p]
D = [0]*2**len(P) # <= 16
G = {}
F = len(D)-1
for i in range(N):
    x = i+1; v = A[i]; b = 0
    for j in range(len(P)):
        if x%P[j]<1:
            b |= 1<<j
            while x%P[j]<1: x //= P[j]
    if x > 1:
        if x not in G: G[x] = []
        G[x].append((b, v))
    else:
        s = F^b
        while 1:
            D[s|b] = max(D[s|b], D[s]+v)
            if s<1: break
            s = (s-1)&(F^b)
for g in G.values():
    E = [*D]
    for b, v in g:
        s = F^b
        while 1:
            E[s|b] = max(E[s|b], D[s]+v)
            if s<1: break
            s = (s-1)&(F^b)
    D = E
print(max(D))