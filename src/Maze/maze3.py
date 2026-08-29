import sys; input = sys.stdin.readline
N, M = map(int, input().split())
G = [[[] for _ in range(26)] for _ in range(N)]
for _ in range(M):
    a, b, c = input().split()
    a = int(a)-1; b = int(b)-1; c = ord(c[0])-65
    G[a][c] += [b]; G[b][c] += [a]
D = [0]*N; D[0] = 100
for s in input().strip():
    s = ord(s)-65; E = [0]*N
    for i in range(N-1):
        k = len(G[i][s])
        for j in G[i][s]: E[j] += D[i]/k
        if k < 1: E[i] += D[i]
    E[-1] += D[-1]; D = E
print(D[-1])