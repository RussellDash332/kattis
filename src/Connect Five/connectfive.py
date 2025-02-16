P = [[*map(int, input().split())] for _ in range(5)]; Z = 0
while 1:
    P = [[a, b] for a, b in {(a, b) for a, b in P}]
    if len(P) == 1: break
    x = sorted((P[i][0], i) for i in range(len(P)))
    if x[0][0] != x[1][0]: P[x[0][1]][0] += 1; Z += 1; continue
    if x[-2][0] != x[-1][0]: P[x[-1][1]][0] -= 1; Z += 1; continue
    x = sorted((P[i][1], i) for i in range(len(P)))
    if x[0][0] != x[1][0]: P[x[0][1]][1] += 1; Z += 1; continue
    if x[-2][0] != x[-1][0]: P[x[-1][1]][1] -= 1; Z += 1; continue
    break
X = {p[0] for p in P}; Y = {p[1] for p in P}
print(2*(max(X)-min(X)+max(Y)-min(Y))+Z+min(max(X)-min(X),max(Y)-min(Y))*any(x not in (min(X),max(X)) and y not in (min(Y),max(Y)) for x, y in P))