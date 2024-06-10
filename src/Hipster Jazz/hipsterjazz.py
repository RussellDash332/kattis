import sys; input = sys.stdin.readline; from array import *
N, M = map(int, input().split()); G = [[] for _ in range(N)]
for _ in range(M): k, l = map(int, input().split()); G[k-1].append(l-1); G[l-1].append(k-1)
Z = array('b', [1]*N); Q = [*range(N)]
while Q:
    c = 0; i = Q.pop(); t = len(G[i])
    for j in G[i]:
        c += Z[i] == Z[j]
        if 2*c > t:
            Z[i] ^= 1
            for j in G[i]: Q.append(j)
            break
print(''.join('PS'[i] for i in Z))