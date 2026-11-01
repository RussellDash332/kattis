import sys; input = sys.stdin.readline
N = int(input()); G = [[int(x)-1 for x in input().split()[1:]] for _ in range(N)]
J = [[G[i][0] if G[i] else -1 for i in range(N)]]
for _ in range(16):
    j = []; p = J[-1]
    for i in range(N): j += [p[p[i]] if ~p[i] else -1]
    J += [j]
for _ in range(int(input())):
    s, t = input().split(); s = int(s)-1; C = []; c = v = -1
    for i in t.strip():
        if '0'<=i<='9':
            if ~v: v = 10*v+int(i)
            else: v = int(i)
        else:
            if ~c: C += [(c, v if ~v else 1)]
            c = i=='~'; v = -1
    if ~c: C += [(c, v if ~v else 1)]
    for c, v in C:
        if c:
            for b in range(17):
                if v&(1<<b): s = J[b][s]
        else: s = G[s][v-1]
    print(s+1)