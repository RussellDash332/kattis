import sys; input = sys.stdin.readline
def lapjv(mat):
    if len(mat) > len(mat[0]): mat = [*map(list, zip(*mat))]
    n, m = len(mat), len(mat[0]); D = [0]*m; P = [0]*m; mtc = [-1]*n; cm = [-1]*m; C = [*range(m)]; pr = [0]*m; d = 0
    for i in range(n):
        for c in range(m): D[c] = mat[i][c]-P[c]; pr[c] = i
        s = t = x = z = 0
        while z^1:
            if s == t:
                x = s; d = D[C[t]]; t += 1
                for j in range(t, m):
                    if d < D[c:=C[j]]: continue
                    if d > D[c]: d = D[c]; t = s
                    C[j], C[t] = C[t], C[j]; t += 1
                for j in range(s, t):
                    if cm[c:=C[j]] < 0: z = 1; break
                if z: break
            r = cm[e:=C[s]]; s += 1
            for j in range(t, m):
                if D[c:=C[j]] <= (v:=mat[r][c]-mat[r][e]+P[e]-P[c]+d): continue
                D[c] = v; pr[c] = r
                if v == d:
                    if cm[c] < 0: z = 1; break
                    C[j], C[t] = C[t], C[j]; t += 1
            if z: break
        for j in range(x): P[C[j]] += D[C[j]]-d
        r = -1
        while r != i: r = cm[c] = pr[c]; c, mtc[r] = mtc[r], c
    return sum(mat[i][mtc[i]] for i in range(n))
N = int(input())
H = []; Z = 0
for _ in range(N):
    x, y = map(int, input().split()); Z += abs(y-x)
    if x > y: x, y = y, x
    H.append([max(0, i-y, x-i) for i in range(1, N+1)])
print(Z+2*lapjv(H))