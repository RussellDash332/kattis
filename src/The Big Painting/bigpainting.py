import sys; input = sys.stdin.readline; from collections import *
def build(pp):
    A = 2
    a = [[[-1]*A, 0, -1, []]]
    for w in range(len(pp)):
        n = 0
        for i in range(len(pp[w])):
            idx = ord(pp[w][i])-48
            if a[n][0][idx] == -1: a[n][0][idx] = len(a); a.append([[-1]*A, 0, -1, []])
            n = a[n][0][idx]
        a[n][3].append(w); n = 0
    q = deque()
    for k in range(A):
        if a[0][0][k] == -1:    a[0][0][k] = 0
        elif a[0][0][k] > 0:    a[a[0][0][k]][1] = 0; q.append(a[0][0][k])
    while q:
        r = q.popleft()
        for k in range(A):
            arck = a[r][0][k]
            if arck != -1:
                q.append(arck)
                v = a[r][1]
                while a[v][0][k] == -1: v = a[v][1]
                a[arck][1] = a[arck][2] = a[v][0][k]
                while a[arck][2] != -1 and not a[a[arck][2]][3]: a[arck][2] = a[a[arck][2]][2]
    return a
def match(s, pp, a):
    matches = Counter(); state = ss = 0
    for i in range(len(s)):
        idx = ord(s[i])-48
        while a[ss][0][idx] == -1: ss = a[ss][1]
        a[state][0][idx] = a[ss][0][idx]; state = a[state][0][idx]; ss = state
        while ss != -1:
            for w in a[ss][3]: matches[w] |= 1<<(i+1-len(pp[w]))
            ss = a[ss][2]
        ss = state
    return matches
r, c, R, C = map(int, input().split()); H = {}
for i in range(r):
    s = input().strip().replace('x', '0').replace('o', '1')
    if s not in H: H[s] = []
    H[s].append(i)
T = [*H]; U = [-1]*r; V = {}; M = []; A = build(T)
for i in range(len(T)):
    for j in H[T[i]]: U[j] = i
for i in range(R):
    s = input().strip().replace('x', '0').replace('o', '1'); t = int(s, 2)
    if t not in V: V[t] = match(s, T, A)
    M.append(t)
Z = 0
for i in range(R-r+1):
    s = V[M[i]][U[0]]
    for j in range(1, r): s &= V[M[i+j]][U[j]]
    Z += bin(s).count('1')
print(Z)