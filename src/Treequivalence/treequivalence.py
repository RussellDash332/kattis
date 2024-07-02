def parse(s):
    L = [i for i in s if 'A'<=i<='Z']; N = len(L); T = [[] for _ in L]; S = []; B = 0; V = [1]*N; R = [N-1]*N; U = [0]; W = [(0, -1)]; A = []
    for i in s[1:]:
        if i == '(': S.append(B)
        elif i == ')': S.pop()
        if 'A'<=i<='Z': B += 1; T[S[-1]].append(B)
    while U:
        u, b = divmod(U.pop(), 2)
        if b:
            for v in T[u]: V[u] += V[v]
        else:
            U.append(2*u+1)
            for v in T[u]: U.append(2*v)
    while W:
        ub, p = W.pop(); u, b = divmod(ub, 2)
        if b:
            if u: A.append((L[u], R[u]))
        else:
            if p != -1: A.append((L[p], V[u])); R[p] -= V[u]
            if not T[u]: A.append((L[u], R[u])); continue
            W.append((2*u+1, -1))
            for v in T[u][::-1]: W.append((2*v, u))
    return ''.join(i+chr(j) for i, j in A)
for _ in range(int(input())): print(['different', 'same'][parse(input().strip()) in 2*parse(input().strip())])