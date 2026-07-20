import sys; input = sys.stdin.readline
N, L, D = map(int, input().split())
S = [input().strip() for _ in range(N)]; C = [*S[0]]
d = [{i for i in range(L) if C[i]!=s[i]} for s in S]
def f(p):
    if p < 0: return
    r = max(range(N), key=lambda x: len(d[x]))
    if len(d[r]) <= D: print(''.join(C)); exit()
    if len(d[r]) > D+p: return
    for k in [*d[r]][:D+1]:
        o = C[k]; C[k] = S[r][k]
        for i in range(N):
            if S[i][k] != C[k]: d[i].add(k)
            else: d[i].discard(k)
        f(p-1); C[k] = o
        for i in range(N):
            if S[i][k] != C[k]: d[i].add(k)
            else: d[i].discard(k)
f(D); print(0)