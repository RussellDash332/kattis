import sys; input = sys.stdin.readline
W = set(); P = 31; M = 10**9+7; I = pow(P, -1, M); E = [pow(P, i, M) for i in range(80)]
while (s:=input().strip()) != '***':
    for w in s.split(): W.add(''.join(filter(str.isalpha, w)).lower())
W = [i for i in W if i]; G = {i:[] for i in W}; H = [[0] for _ in W]; R = [[] for _ in W]; ok = 0
for i in range(len(W)):
    h = H[i]; N = len(W[i])
    for j in range(N): h.append((h[-1]*P+ord(W[i][j])-96)%M)
    for j in range(N): R[i].append((h[N]-h[j]*E[N-j]-(ord(W[i][j])-96-h[j])*E[N-j-1])%M)
for i in range(len(W)):
    for j in range(i+1, len(W)):
        if H[j][-1] in R[i] or H[i][-1] in R[j]: G[W[i]].append(W[j]); G[W[j]].append(W[i])
        elif len(W[i]) == len(W[j]):
            fd = 0
            for k in range(len(W[i])):
                if R[i][k] == R[j][k]: fd = 1; G[W[i]].append(W[j]); G[W[j]].append(W[i]); break
            if not fd:
                c = []
                for k in range(len(W[i])):
                    if W[i][k] != W[j][k]: c.append(k)
                if len(c) == 2 and W[i][c[0]] == W[j][c[1]] != W[i][c[1]] == W[j][c[0]]: G[W[i]].append(W[j]); G[W[j]].append(W[i])
for i in sorted(W):
    if G[i]: print(f'{i}:', *sorted(G[i])); ok = 1
if not ok: print('***')