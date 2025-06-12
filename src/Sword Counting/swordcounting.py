import sys; input = sys.stdin.readline
N, M = map(int, input().split())
G = [set() for _ in range(N)]
for _ in range(M): a, b = map(int, input().split()); G[a-1].add(b-1); G[b-1].add(a-1)
H = [i for i in range(N) if len(G[i])**2 >= N]
L = [i for i in range(N) if len(G[i])**2 < N]
B = [0]*N
for i in H: B[i] = 1
Z = X = 0
def C(n): return n*(n-1)
for p in range(N):
    for q in G[p]: Z += (len(G[p])-1)*(len(G[p])-2)*(len(G[p])-3)*(len(G[q])-1)//6
for i in range(len(H)):
    for j in range(i):
        if H[j] not in G[H[i]]: continue
        for k in range(j):
            if H[k] in G[H[i]] and H[k] in G[H[j]]: Z -= C(len(G[H[i]])-2)+C(len(G[H[j]])-2)+C(len(G[H[k]])-2)
for i in L:
    for j in G[i]:
        for k in G[i]&G[j]: X += (C(len(G[i])-2)+C(len(G[j])-2)+C(len(G[k])-2))*(2, 3, 6)[B[j]+B[k]]
print(Z-X//12)