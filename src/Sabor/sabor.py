import sys; input = sys.stdin.readline; from array import *
N = int(input()); G = [[] for _ in range(N)]
for _ in range(5):
    P, *K = map(int, input().split())
    for i in range(P): k = K[2*i]-1; l = K[2*i+1]-1; G[k].append(l); G[l].append(k)
Z = array('b', [1]*N); Q = [*range(N)]
while Q:
    c = 0; i = Q.pop()
    for j in G[i]:
        c += Z[i] == Z[j]
        if c == 3:
            Z[i] ^= 1
            for j in G[i]: Q.append(j)
            break
print(''.join(chr(i+65) for i in Z))