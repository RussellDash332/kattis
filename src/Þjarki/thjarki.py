import sys; input = sys.stdin.readline
R, C = map(int, input().split()); G = [*range(R*C)]
for r in range(R):
    M = input()
    for c in range(C):
        if M[c] == '>' and c < C-1: G[r*C+c] = r*C+c+1
        if M[c] == '<' and c > 0: G[r*C+c] = r*C+c-1
        if M[c] == '^' and r > 0: G[r*C+c] = r*C+c-C
        if M[c] == 'v' and r < R-1: G[r*C+c] = r*C+c+C
J = [[*G]]
for i in range(32): p = J[i]; J.append([p[p[j]] for j in range(R*C)])
for _ in range(int(input())):
    r, c, k = map(int, input().split()); p = (r-1)*C+c-1
    for i in range(31, -1, -1):
        if k&(1<<i): p = J[i][p]
    print(p//C+1, p%C+1)