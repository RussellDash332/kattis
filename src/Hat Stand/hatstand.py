K, N, *A = map(int, open(0).read().split()); A = [i-1 for i in A]
F = [-1]*K; J = [-1]*N; Z = []
for i in range(N-1, -1, -1): J[i] = F[A[i]]; F[A[i]] = i
for i in range(K):
    z = 0; k = F[i]
    while ~k: z += 1; k = J[k-1]
    Z += [z]
H = sorted([i+1 for i in range(K) if i-A[0]], key=lambda x: -Z[x-1])
I = [*H]; R = {e-1:i for i,e in enumerate(I)}; C = 0; c = A[0]
for i in A[1:]: k = R[i]; C += k+1; R[c] = k; I[k], c = c, i
print(C, *H)