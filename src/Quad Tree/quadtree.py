INF = 10**9; t, K = map(int, input().split()); G = [[*map(int, input())] for _ in range(t)]; P = [[0]*(t+1) for _ in range(t+1)]
for i in range(t):
    for j in range(t): P[i+1][j+1] = P[i][j+1]+P[i+1][j]-P[i][j]+G[i][j]
def dp(r, c, s):
    T = s*s; O = P[r+s][c+s]-P[r][c+s]-P[r+s][c]+P[r][c]; Z = T-O; R = {O:1, T-O:1}
    if s > 1:
        h = s//2; Q = [dp(r, c, h), dp(r, c+h, h), dp(r+h, c, h), dp(r+h, c+h, h)]; C = Q[0]
        for q in Q[1:]:
            N = {}
            for c1, n1 in C.items():
                for c2, n2 in q.items():
                    tc, tn = c1+c2, n1+n2
                    if tc not in N or tn < N[tc]: N[tc] = tn
            C = N
        for k, v in C.items():
            if k not in R or v+1 < R[k]: R[k] = v+1
    S = sorted(R.items()); D = {}; m = INF
    for k, v in S:
        if v < m: D[k] = m = v
    return D
print(min(v for k, v in dp(0, 0, t).items() if k <= K))