import sys; input = sys.stdin.readline
for _  in range(int(input())):
    M = [input().strip() for _ in range(int(input()))]
    S = input().strip(); D = input().strip(); N = len(S); T = len(D); z = ['?']*T
    M = [i for i in M if len(i) == N]; can = 0
    W = {chr(i+97):set() for i in range(26)}
    for m in M:
        a = {}; r = {}; ok = 1
        for i in range(N):
            if m[i] not in a: a[m[i]] = S[i]
            if S[i] not in r: r[S[i]] = m[i]
            if a[m[i]] != S[i] or r[S[i]] != m[i]: ok = 0; break
        if ok:
            can = 1
            for i in S: W[i].add(r[i])
    if not can: print('IMPOSSIBLE'); continue
    if all(len(v)<2 for v in W.values()) and sum(len(v) for v in W.values()) == 25:
        for i in W:
            if not W[i]:
                t = {chr(i) for i in range(97, 123)}
                for j in W: t -= W[j]
                W[i] = t; break
    K = {chr(i+97):set() for i in range(26)}
    for i in W:
        for j in W[i]: K[j].add(i)
    for i in range(T):
        u = K[D[i]]
        if len(u) == 1:
            u = [*u][0]
            if len(W[u]) == 1: z[i] = u
    print(''.join(z))