import sys; input = sys.stdin.readline
M = 101; A, B = [0]*M, [0]*M
for _ in range(int(input())):
    a, b = map(int, input().split()); A[a] += 1; B[b] += 1; C, D = A.copy(), B.copy()
    pa, pb = 0, M-1; ans = 0
    while pa < M and pb >= 0:
        if A[pa] and B[pb]: x = min(A[pa], B[pb]); A[pa] -= x; B[pb] -= x; ans = max(ans, pa+pb)
        elif A[pa]: pb -= 1
        elif B[pb]: pa += 1
        else: pb -= 1; pa += 1
    A, B = C, D; print(ans)