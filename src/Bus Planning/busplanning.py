import sys; input = sys.stdin.readline
B = [x.bit_count() for x in range(2<<17)]
def bt(v, cc):
    global Z, A
    if cc >= Z: return
    if v == n: Z = cc; A = [*cl]; return
    for i in range(1, cc+2):
        if B[cm[i]] < c and cm[i]&am[v] == cm[i]: cl[v] = i; cm[i] |= 1<<v; bt(v+1, max(cc, i)); cm[i] ^= 1<<v; cl[v] = 0
n, m, c = map(int, input().split())
G = [[1]*n for _ in range(n)]; vv = [input().strip() for _ in range(n)]; r = {}
for i in range(n): r[vv[i]] = i
for _ in range(m): a, b = input().strip().split(); G[r[a]][r[b]] = G[r[b]][r[a]] = 0
am = [0]*n
for i in range(n):
    for j in range(n):
        if G[i][j]: am[i] |= 1<<j
Z, A = n+1, []; cl = [0]*n; cm = [0]*(n+1); bt(0, 0); cc = {}
for i in range(n):
    if A[i] == 0: continue
    if A[i] not in cc: cc[A[i]] = []
    cc[A[i]].append(i)
print(Z)
for i in cc.values(): print(*map(lambda x: vv[x], i))