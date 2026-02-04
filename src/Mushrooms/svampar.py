N, *W = map(int, open(0).read().split()); A = [0]*N; x = next(i for i in range(N) if W.count(W[i]) > 1); y = next(i for i in range(x+1, N) if W[i] == W[x]); print(9); r = ['p']*N; r[x] = f'+ {y+1}'; A[x] = 1; print(*r)
for _ in range(7):
    r = ['p']*N; r[x] = f'< {x+1}'
    for i in range(N):
        if i != x and (W[i]-(i==y)*(0<W[x]<129))&A[x]: r[i] = f'| {x+1}'; A[i] |= A[x]
    A[x] *= 2; print(*r)
r = ['p']*N
for i in range(N):
    if i != x and W[i]>=128: r[i] = f'| {x+1}'
if W[x] > 128: r[x] = f'| {y+1}'; r[y] = f'| {x+1}'
elif W[x]: r[x] = r[y] = f'+ {y+1}'
else: r[x] = f'& {y+1}'
print(*r)