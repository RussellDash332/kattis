import sys; input = sys.stdin.readline
N = int(input()); K = lambda: print('impossible')<exit()
J = []; C = []; force = 0; H = [[] for _ in range(2*N+2)]
for i in range(N):
    a, b, c, d = map(int, input().split()); J += [(a, b, c, d)]
    if [a, b, c, d].count(0) == 3: force = 1
    for j in J[-1]:
        if j: H[j] += [i]
if N == 1:
    if J != [(0, 0, 0, 0)]: K()
    else: print(1, 1, 1); exit()
for i, (a, b, c, d) in enumerate(J):
    if [a, b, c, d].count(0) == 2+force: C += [i]
if len(C) not in (2, 4): K()
s = C[0]; a, b, c, d = J[s]; t = 0; U = [0]*N
while t<4 and (a or b): a, b, c, d = b, c, d, a; t += 1
if t==4 and (a or b): K()
Z = [[(s, a, b, c, d)]]; U[s] = 1
while c:
    s = sum(H[c])-s; a2, b2, c2, d2 = J[s]; t = 0
    if U[s]: K()
    while t<4 and (a2 != c or b2): a2, b2, c2, d2 = b2, c2, d2, a2; t += 1
    if t==4 and (a2 != c or b2): K()
    a, b, c, d = a2, b2, c2, d2; Z += [[(s, a, b, c, d)]]; U[s] = 1
    if s in C: break
s, a, b, c, d = Z[0][0]
while d:
    s = sum(H[d])-s; a2, b2, c2, d2 = J[s]; t = 0
    if U[s]: K()
    while t<4 and (b2 != d or a2): a2, b2, c2, d2 = b2, c2, d2, a2; t += 1
    if t==4 and (b2 != d or a2): K()
    a, b, c, d = a2, b2, c2, d2; Z[0] += [(s, a, b, c, d)]; U[s] = 1
    if s in C: break
R, W = len(Z), len(Z[0])
if R*W != N: K()
for i in range(1, R):
    for j in range(1, W):
        s = sum(H[Z[i][j-1][4]])-Z[i][j-1][0]; a, b, c, d = J[s]; t = 0
        if U[s]: K()
        while t<4 and (a!=Z[i-1][j][3] or b!=Z[i][j-1][4]): a, b, c, d = b, c, d, a; t += 1
        if t==4 and (a!=Z[i-1][j][3] or b!=Z[i][j-1][4]): K()
        if (i==R-1 and c) or (j==W-1 and d): K()
        Z[i] += [(s, a, b, c, d)]; U[s] = 1
print(R, W)
for z in Z: print(*(u[0]+1 for u in z))