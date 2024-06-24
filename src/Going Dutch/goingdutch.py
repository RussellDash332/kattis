import sys; input = sys.stdin.readline; from array import *
V, E = map(int, input().split()); M = [0]*V; R = {1<<i: i for i in range(V)}; D = array('i', [-1]*(1<<V)); B = array('i', [0]*(1<<V))
for _ in range(E): a, b, w = map(int, input().split()); M[a] -= w; M[b] += w
for i in range(1, 1<<V): B[i] = B[i-(i&-i)]+M[R[i&-i]]
def dp(bm):
    if bm == 0: return 0
    if D[bm] != -1: return D[bm]
    bm2 = bm; ans = 0
    while bm2: nxt = bm2&-bm2; bm2 ^= nxt; ans = max(ans, dp(bm^nxt))
    D[bm] = ans+(B[bm]==0); return D[bm]
print(V-dp(2**V-1))