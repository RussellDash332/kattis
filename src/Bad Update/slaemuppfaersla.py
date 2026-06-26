def f(x):
    q = [0]*N
    for i in range(N): u = min(x, V[i]); q[i] = u; x -= u
    print('?', *q)
    return input()<'V'
N = int(input())
V = [int(input()) for _ in range(N)]
lo, hi = 0, sum(V)
while hi-lo>1:
    if f(mi:=(lo+hi)//2): lo = mi
    else: hi = mi
for i in range(N):
    if hi <= V[i]: print('!', i+1, hi); break
    hi -= V[i]