import sys; input = sys.stdin.readline
V = int(input()); I = [0]*V; G = [[] for _ in range(V)]; S = [0]*V; A = 0; C = []
for i in range(V): j = int(input())-1; I[j] += 1; G[i].append(j); G[j].append(i)
for i in range(V):
    if S[i] == 0:
        q = [i]; c = []
        for u in q:
            if S[u]: continue
            c.append(u); S[u] = 1; q.extend(G[u])
        C.append(c)
for c in C: A += max(sum(max(I[j]-1, 0) for j in c), len(C)>1)
print(A)