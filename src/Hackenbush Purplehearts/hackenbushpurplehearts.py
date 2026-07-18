import sys; input = sys.stdin.readline
N = int(input()); T = [[] for _ in range(N)]; R = []
for i, p in enumerate(map(int, input().split())): (T[p-1] if ~p else R).append(i)
S = [(2*(s<'R')-1, 0) for s in input().strip()]
def reduce(p, q):
    while p%2<1 and q: p //= 2; q -= 1
    return p, q
def add(p, q, a, b):
    m = max(q, b); p, q = (p<<(m-q))+(a<<(m-b)), m
    return reduce(p, q)
for i in range(N-1, -1, -1):
    p = q = 0
    for j in T[i]: p, q = add(p, q, *S[j])
    if S[i][0]>0: # blue
        if p < 0: k = (-p)>>q; p += (k+2)<<q; q += k+1
        else: p += 1<<q
    else: # red
        if p > 0: k = p>>q; p -= (k+2)<<q; q += k+1
        else: p -= 1<<q
    S[i] = reduce(p, q)
p = q = 0
for i in R: p, q = add(p, q, *S[i])
print(f'{p}/2^{q}' if q else p)