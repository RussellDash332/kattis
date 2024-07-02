import sys; input = sys.stdin.readline
R = dict(zip('AGTC', range(4)))

def solve(N, CNF):
    G = [[] for _ in range(2*N)]; Gt = [[] for _ in range(2*N)]; T, V, S = [], [0]*2*N, 1
    for (a, p), (b, q) in CNF: G[a+N*(1-p)].append(b+N*q); G[b+N*(1-q)].append(a+N*p)
    for i in range(2*N):
        for j in G[i]: Gt[j].append(i)
    def DFS(s, t):
        U = [2*s]; a = G if t else Gt
        while U:
            ub = U.pop()
            u, b = ub//2, ub%2
            if b and t: T.append(u)
            elif V[u] == 0:
                V[u] = S; U.append(2*u+1)
                for v in a[u]:
                    if V[v] == 0: U.append(2*v)
        return 1
    for i in range(2*N):
        if V[i] == 0: DFS(i, 1)
    V = [0]*2*N
    for i in T[::-1]:
        if V[i] == 0: S += DFS(i, 0)
    return any(V[i]==V[i+N] for i in range(N))


while True:
    n, m = map(int, input().split())
    if not n: break
    s = [R[i] for i in input().strip()]; CNF = []
    # cannot modify two consecutive
    # -c_a v -c_b
    for i in range(n-1): CNF.append(((2*i, 1), (2*(i+1), 1)))
    # if changed, must either increase or decrease
    # -d_a v c_a
    for i in range(n): CNF.append(((2*i+1, 1), (2*i, 0)))
    for _ in range(m):
        k, *p = map(int, input().replace(':', '').split())
        for i in range(k//2):
            if s[p[i]] == s[p[-i-1]]:
                # both unchanged or both changed in the same direction
                # (c_a == c_b) ^ (d_a == d_b)
                # (c_a v -c_b) ^ (-c_a v c_b) ^ (d_a v -d_b) ^ (-d_a v d_b)
                CNF.append(((2*p[i], 0), (2*p[-i-1], 1)))
                CNF.append(((2*p[i], 1), (2*p[-i-1], 0)))
                CNF.append(((2*p[i]+1, 0), (2*p[-i-1]+1, 1)))
                CNF.append(((2*p[i]+1, 1), (2*p[-i-1]+1, 0)))
            elif (s[p[i]]-s[p[-i-1]])%4 != 2:
                # exactly one must be changed to the other's
                # (c_a v c_b) ^ (-c_a v -c_b)
                CNF.append(((2*p[i], 0), (2*p[-i-1], 0)))
                CNF.append(((2*p[i], 1), (2*p[-i-1], 1)))
                if (s[p[i]]-s[p[-i-1]])%4 == 3:
                    # (c_a -> -d_a) ^ (c_b -> d_b) -> increase a or decrease b
                    # (-c_a v -d_a) ^ (-c_b v d_b)
                    CNF.append(((2*p[i], 1), (2*p[i]+1, 1)))
                    CNF.append(((2*p[-i-1], 1), (2*p[-i-1]+1, 0)))
                else:
                    # (c_a -> d_a) ^ (c_b -> -d_b) -> decrease a or increase b
                    # (-c_a v d_a) ^ (-c_b v -d_b)
                    CNF.append(((2*p[i], 1), (2*p[i]+1, 0)))
                    CNF.append(((2*p[-i-1], 1), (2*p[-i-1]+1, 1)))
            else:
                # both must be changed in reverse direction
                # c_a ^ c_b ^ (d_a v d_b) ^ (-d_a v -d_b)
                CNF.append(((2*p[i], 0), (2*p[i], 0)))
                CNF.append(((2*p[-i-1], 0), (2*p[-i-1], 0)))
                CNF.append(((2*p[i]+1, 0), (2*p[-i-1]+1, 0)))
                CNF.append(((2*p[i]+1, 1), (2*p[-i-1]+1, 1)))
    print('YNEOS'[solve(2*n, CNF)::2]); input()
