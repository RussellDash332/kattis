import sys; input = sys.stdin.readline
N, X, Y = map(int, input().split())
C = [{ord(x)-97 for x in input().strip().split()[1]} for _ in range(26)]
W = [[ord(x)-97 for x in input().strip()] for _ in range(N)]
S = [set() for _ in range(26)]; P = []
for w in W:
    n = len(w); ok = 1
    for i in range(n-1):
        if w[i+1] not in C[w[i]]: ok = 0; break
    P.append(ok)
    if ok: S[w[0]].add(n)
for i, w in enumerate(W):
    e, d = w[-1], len(w); z = 0
    if X <= d <= Y and P[i]: z = 1
    elif d < X:
        for f in C[e]:
            for x in S[f]:
                if X <= d+x <= Y and P[i]: z = 1; break
            if z: break
    sys.stdout.write('FGeelti nmee ogwoto!d !\n\n'[1-z::2])