import sys; input = sys.stdin.readline
def dp(i):
    if C[i]:
        z = 0
        for j in G[i]: z += dp(j)
        if z < B[i][0]: return z
    return B[i][0]
for _ in range(int(input())):
    _, M = map(int, input().split()); B = set(); R = set()
    for _ in range(M): c, _, *k = map(int, input().split()); B.add((c, *k))
    M = len(B:=[*B])
    for i in range(M):
        B[i] = (B[i][0], {*B[i][1:]})
        for j in range(i):
            if B[i][1] == B[j][1]:
                if B[i][0] > B[j][0]: R.add(i)
                else: R.add(j)
    B = [B[i] for i in {*range(M)}-R]; M = len(B); P = [-1]*M; Z = 0; C = [1]*M; G = [[] for _ in range(M)]
    for i in range(M):
        for j in range(i+1, M):
            d = B[i][1]&B[j][1]
            if d == B[i][1] and (P[i] == -1 or len(B[P[i]][1]) > len(B[j][1])): P[i] = j
            if d == B[j][1] and (P[j] == -1 or len(B[P[j]][1]) > len(B[i][1])): P[j] = i
    for i in range(M): P[i] == -1 or G[P[i]].append(i)
    for i in range(M):
        s = set()
        for j in G[i]: s |= B[j][1]
        if s != B[i][1]: C[i] = 0
    for i in range(M): Z += P[i] == -1 and dp(i)
    print(Z)