def mult(A, B):
    C = [0]*(len(A)+len(B)-1)
    for i in range(len(A)):
        if not A[i]: continue
        for j in range(len(B)): C[i+j] += A[i]*B[j]; C[i+j] %= M
    return C
def sub(u, v):
    z = [*u]
    while len(z) < len(v): z.append(0)
    for i in range(len(v)): z[i] -= v[i]; z[i] %= M
    return z
M = 10**9+7; input()
A = [*map(int, input().split())]; O = [*A]
B = [*map(int, input().split())]
Z = [0]*1001
while A:
    while A and A[-1] == 0: A.pop()
    if len(A) >= len(B):
        Z[len(A)-len(B)] = k = A[-1]%M
        A = sub(A, mult([0]*(len(A)-len(B))+[k], B))
    else: break
while Z and Z[-1] == 0: Z.pop()
A = [i%M for i in A]
while A and A[-1] == 0: R.pop()
print(*(Z or [0])); print(*(A or [0]))