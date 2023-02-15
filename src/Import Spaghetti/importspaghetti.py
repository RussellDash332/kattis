INF = float('inf')
def fw(D, v):
    nxt = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        nxt[i][i] = i
        for j in range(n):
            if D[i][j] == 1: nxt[i][j] = j
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    nxt[i][j] = nxt[i][k]
    return nxt

g = {}
n = int(input())
D = [[INF for _ in range(n)] for _ in range(n)]
pkgs = input().strip().split()
rev = dict(map(reversed, enumerate(pkgs)))
for i in range(n):
    for _ in range(int(input().split()[1])):
        imports = input()[7:].strip().split(', ')
        for imps in imports:
            D[rev[imps]][i] = 1
nxt = fw(D, n)
cyc = INF
for i in range(n): cyc = min(cyc, D[i][i])
if cyc == INF: print('SHIP IT')
else:
    for i in range(n):
        if D[i][i] == cyc:
            s = i
            break
    path = [s]
    while len(path) != cyc: path.append(nxt[path[-1]][s])
    print(*map(lambda x: pkgs[x], path[::-1]))