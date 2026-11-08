INF = 1e9; t = 0
while (N:=int(input())):
    P = []; K = []; t += 1
    for _ in range(N): x, y, k = map(int, input().split()); P += [(x+y*1j, k)]; K += [k]
    mst = []; A = [(INF, 0)]*N; B = [0]*N; A[0] = (0, -1)
    while len(mst) != N:
        best = (0, A[0])
        for i in range(1, N):
            if A[i][0] < best[1][0]: best = (i, A[i])
        mst.append(best)
        A[best[0]], B[best[0]] = (INF, 0), 1
        for v in range(N):
            if not B[v] and A[v] > (d:=(abs(P[best[0]][0]-P[v][0]), best[0])): A[v] = d
    D = [0]*N
    for u, (d, p) in mst[1:]: D[u] = max(D[p], d)
    print('Colony Group:', t, 'Average', '%.2f'%(sum(k*d/3 for d, k in zip(D, K))/sum(K)))