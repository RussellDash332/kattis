N, M = map(int, input().split())
A = [*map(int, input().split())]
G = [[] for _ in range(3*N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1] += [b-1]; G[b-1] += [a-1]
S = []; D = []; T = []; V = [0]*3*N
for i in range(3*N):
    if V[i]<1:
        V[i] = 1; Q = [i]
        for u in Q:
            for v in G[u]:
                if V[v]<1: V[v] = 1; Q += [v]
        if len(Q) > 3: print('Impossible'); exit()
        (S, D, T)[len(Q)-1].append((sum(A[j] for j in Q), [j+1 for j in Q]))
S.sort(); D.sort(); T.sort(); I = []
for _ in range(N):
    z = 0; p = []; Z = []
    if len(S)-len(D)>2 and (x:=S[-1][0]+S[-2][0]+S[-3][0]) > z: z = x; p = [0, 0, 0]
    if S and D and (x:=S[-1][0]+D[-1][0]) >= z: z = x; p = [0, 1]
    if T and T[-1][0] > z: z = T[-1][0]; p = [2]
    if z < 1: print('Impossible'); exit()
    for i in p: Z.extend((S, D, T)[i].pop()[1])
    I.append(Z)
print('Possible')
for z in I: print(*z)