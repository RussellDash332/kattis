N, K = map(int, input().split()); A = [*map(int, input().split())]; f = lambda a: sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1, len(a)))
# if K == N, you can either reverse it or not
if K == N:
    if (x:=f(A)) <= (y:=f(A[::-1])): print(x, 0)
    else: print(y, 1, '1'*N)
    exit(0)
# otherwise, we can always sort it in (N-K)+2(K+1) = N+K+2 moves
# take K-1 smallest and the i-th smallest where i = N-1, N-2, ..., K+1
# -> this will ensure that the N-(K+1) largest [K+1..N-1] will be in a relative sorted order
# then take K+1 smallest minus the i-th smallest where i = 0, 1, 2, ..., K + flip these
# -> this will clump [K+1..N-1] together while ordering [0..K] on the left side like it's insertion sort
B = sorted((e,i) for i,e in enumerate(A)); M = []; F = '1'*K+'0'*(N-K)
for i in range(N): A[B[i][1]] = i
for i in range(N-1, K, -1):
    L, R, T = [], [], ''
    for j in A:
        if j < K-1 or j == i: L.append(j); T += '1'
        else: R.append(j); T += '0'
    A = L[::-1]+R; M.append(T)
for i in range(K+1):
    L, R, T = [], [], ''
    for j in A:
        if j <= K and j != i: L.append(j); T += '1'
        else: R.append(j); T += '0'
    A = L+R; M.append(T); M.append(F)
print(0, len(M), *M)