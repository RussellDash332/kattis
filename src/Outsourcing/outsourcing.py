import sys; input = sys.stdin.readline
for _ in range(int(input())):
    M1, N1, K1, M2, N2, K2 = map(int, input().split()); K = min(K1, K2)
    T1 = [[N1]*K for _ in range(N1+1)]; T2 = [[N2]*K for _ in range(N2+1)]
    for _ in range(M1):
        tin, tout, s = map(int, input().split())
        if s < K: T1[tin][s] = tout
    for _ in range(M2):
        tin, tout, s = map(int, input().split())
        if s < K: T2[tin][s] = tout
    N1 += 1; N2 += 1; T = [[T1[i//N2][j]*N2+T2[i%N2][j] for j in range(K)] for i in range(N1*N2)]; Q = [0]; V = set()
    for u in Q:
        if (u//N2==N1-2)^(u%N2==N2-2): print('not eligible'); break
        if u in V: continue
        V.add(u); Q.extend(T[u])
    else: print('eligible')