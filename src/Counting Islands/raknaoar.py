import sys; input = sys.stdin.readline; from heapq import *; from array import *
N, Q = map(int, input().split()); P = []; H = array('I', [0]*N); S = []; M = 0; V = array('i'); Z = {}; C = N+3
for i in range(N):
    _, *v = map(int, input().split())
    for u in v: P.append(-u*C+i)
for _ in '.'*Q: P.append((x:=-int(input()))*C+N); V.append(-x)
for c in sorted(P):
    x, k = c//C, c%C
    print(x, k)
    if k == N: Z[-x] = -S[0]+1 if S else N
    else:
        H[k] += 1
        if M < H[k]: M = H[k]; S = []
        if M == H[k]: heappush(S, -k)
for v in V: sys.stdout.write(str(Z[v])+'\n')