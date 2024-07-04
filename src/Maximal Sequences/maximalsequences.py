import sys; input = sys.stdin.readline
N = int(input()); A = [*map(int, input().split())]; H = {}
for i in range(N):
    if A[i] not in H: H[A[i]] = []
    H[A[i]].append(i)

# make bisect non-imported
def f(x):
    z = -S
    for i in Q:
        l, h = 0, len(i)
        while l < h:
            m = (l+h)//2
            if x < i[m]: h = m
            else: l = m+1
        z += l
    return z >= x

for _ in range(int(input())):
    K, _, *Q = map(int, input().split()); K -= 1; lo, hi = K-1, N-1; Q = [H[i] for i in Q if i in H]; S = 1-K
    for i in Q:
        l, h = 0, len(i)
        while l < h:
            m = (l+h)//2
            if i[m] < K: l = m+1
            else: h = m
        S += l
    while hi-lo>1:
        if f(mi:=(lo+hi)//2): lo = mi
        else: hi = mi-1
    print((hi if f(hi) else hi-1)-K+1)