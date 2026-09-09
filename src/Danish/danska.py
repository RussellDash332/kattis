from collections import *
N, M = map(int, input().split())
W = [input() for _ in range(M)]
A = 26
a = [[[-1]*A, 0, -1, []]]
B = [0]
for w in W:
    n = 0
    for i in range(len(w)):
        idx = ord(w[i])-97
        if a[n][0][idx] == -1: a[n][0][idx] = len(a); a.append([[-1]*A, 0, -1, []]); B += [0]
        n = a[n][0][idx]
    a[n][3].append(w); B[n] = 1
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
            #while a[arck][2] != -1 and not a[a[arck][2]][3]: a[arck][2] = a[a[arck][2]][2]
            B[arck] |= B[a[arck][1]]
        else:
            a[r][0][k] = a[a[r][1]][0][k]
D = [0]*len(a); D[0] = 1; MOD = 10**9+7
for i in range(N):
    E = [0]*len(a)
    for j in range(len(a)):
        if B[j] or D[j]<1: continue
        for k in range(A):
            if B[v:=a[j][0][k]]<1: E[v] = (E[v]+D[j])%MOD
    D = E
print(sum(D)%MOD)