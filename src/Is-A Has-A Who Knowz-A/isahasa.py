import sys; input = sys.stdin.readline
MAXN = 500
n, m = map(int, input().split())
mi = [[0]*MAXN for _ in range(MAXN)]
mh = [[0]*MAXN for _ in range(MAXN)]
rev = {}
for _ in range(n):
    f, r, l = input().strip().split()
    if f not in rev: rev[f] = len(rev)
    if l not in rev: rev[l] = len(rev)
    if r[0] == 'i': mi[rev[f]][rev[l]] = 1
    else: mh[rev[f]][rev[l]] = 1
MAXN = len(rev)
for i in range(MAXN): mi[i][i] = 1
MI = [[mi[i][j] for j in range(MAXN)] for i in range(MAXN)]
MH = [[mh[i][j] for j in range(MAXN)] for i in range(MAXN)]
for k in range(MAXN):
    for i in range(MAXN):
        for j in range(MAXN):
            MI[i][j] |= MI[i][k] & MI[k][j]
            MH[i][j] |= (MH[i][k] & MH[k][j]) | (MI[i][k] & MH[k][j]) | (MH[i][k] & MI[k][j])
ft = ['false', 'true']
for q in range(1, m+1):
    f, r, l = input().strip().split()
    if r[0] == 'i': print(f'Query {q}:', ft[MI[rev[f]][rev[l]]])
    else: print(f'Query {q}:', ft[MH[rev[f]][rev[l]]])