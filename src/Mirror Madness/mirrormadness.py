import sys; input = sys.stdin.readline
N, M = map(int, input().split()); P = []
for _ in range(N):
    x, y = map(int, input().split())
    P += [(x+y, y-x)]
Q = [P[0]]
for i in range(N):
    x1, y1 = P[i]; x2, y2 = P[(i+1)%N]; s = (y1<y2)-(y1>y2)
    if x1+y1 == x2+y2:
        for k in range(s, s*(abs(y1-y2)+1), s): Q += [(x1-k, y1+k)]
    else:
        for k in range(s, s*(abs(y1-y2)+1), s): Q += [(x1+k, y1+k)]
X = {}; Y = {}; R = {}; S = {}
for x, y in sorted(Q):
    if x not in X: X[x] = []; R[x] = {}
    if y not in Y: Y[y] = []; S[y] = {}
    R[x][y] = len(X[x]); S[y][x] = len(Y[y]); X[x] += [y]; Y[y] += [x]
x0, y0 = map(int, input().split()); x, y = x0+y0, y0-x0; f = 0
for _ in range(M):
    if f: x, y = y, x
    x, y = Y[y][S[y][x]^1], y
    if f: x, y = y, x
    print((x-y)>>1, (x+y)>>1); X, Y, R, S = Y, X, S, R; f ^= 1