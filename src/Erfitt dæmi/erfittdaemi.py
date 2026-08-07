import sys; input = sys.stdin.readline; print = sys.stdout.write
N, M = map(int, input().split()); C = [[] for _ in range(2*N)]; P = [8, 4, 2, 1]; V = [3]*M; S = [0]*M
for i in range(M):
    a, b, c = input().split(',')
    a = int(a.split('!')[-1])+N*(a[0]=='!')-1
    b = int(b.split('!')[-1])+N*(b[0]=='!')-1
    c = int(c.split('!')[-1])+N*(c[0]=='!')-1
    C[a] += [i]; C[b] += [i]; C[c] += [i]
for i in range(N):
    p = 0
    for j in C[i]:
        if 1-S[j]: p += P[V[j]]
    for j in C[i+N]:
        if 1-S[j]: p -= P[V[j]]
    if p < 0:
        print('OSATT\n')
        for j in C[i+N]: S[j] = 1
        for j in C[i]: V[j] -= 1-S[j]
    else:
        print('SATT\n')
        for j in C[i]: S[j] = 1
        for j in C[i+N]: V[j] -= 1-S[j]