N = min(int(input()), 28); K = 10**6; P = []
for i in range(N): x, y = map(int, input().split()); P.append(x*K+y)
def ans(a, b):
    print('no'); A = []; B = []
    for i in range(N):
        if a%3 == 1 or b%3 == 2: A.append(i+1)
        elif a%3 == 2 or b%3 == 1: B.append(i+1)
        a //= 3; b //= 3
    print(len(A), *A); print(len(B), *B); exit()
H = {K//2: 0}; E = {K//2: 0}
for i in range(N//2):
    p = P[i]; U = {**H}
    for k in H: U[k+p] = H[k]+3**i; U[k-p] = H[k]+2*3**i
    H = U
for i in range(N//2, N):
    p = P[i]; U = {**E}
    for k in E: U[k+p] = E[k]+3**i; U[k-p] = E[k]+2*3**i
    E = U
for i in H: i in E and i != K//2 > ans(E[i], H[i])
print('yes')