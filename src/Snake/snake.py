R, C = map(int, input().split()); M = [input() for _ in range(R)]; S = tuple((i, j) for x in '0123456789abcdef' for i in range(R) for j in range(C) if M[i][j] == x); K = ((0, -1), (-1, 0), (1, 0), (0, 1)); V = {S}; T = [S]
if len(S) == 1: print(1); exit()
while T:
    u = T.pop()
    for dr, dc in K:
        v = (u[0][0]+dr, u[0][1]+dc)
        if R>v[0]>-1<v[1]<C and v != u[1] and v not in u[:-1]:
            if M[v[0]][v[1]] == 'A': print(1); exit()
            w = (v, *u[:-1])
            if w not in V: V.add(w); T.append(w)
print(0)