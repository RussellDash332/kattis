from collections import deque; from random import *
import sys; input = sys.stdin.readline
N, M, K = map(int, input().split()); pp = []; H = [0]*N; A = 27; a = [[[-1]*A, 0, -1, []]]
for w in range(N):
    n = 0; s = input().strip().replace(' ', '`')
    for i in range(len(s)):
        idx = ord(s[i])-96
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
for _ in range(M): x, y = map(int, input().split()); r = randint(1, 10**9); H[x-1] += r; H[y-1] -= r
T = {}
for _ in range(K):
    s = input().strip().replace(' ', '`')
    if s in T: sys.stdout.write(T[s]); continue
    state = ss = 0; z = 0
    for i in range(len(s)):
        idx = ord(s[i])-96
        while a[ss][0][idx] == -1: ss = a[ss][1]
        state = a[ss][0][idx]; ss = state
        while ss != -1:
            for w in a[ss][3]: z += H[w]
            ss = a[ss][2]
        ss = state
    T[s] = 'yneos\n\n'[z!=0::2]; sys.stdout.write(T[s])