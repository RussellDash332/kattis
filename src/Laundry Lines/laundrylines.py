N, *W = map(int, open(0).read().split()); B = 2**N-1
def ok(Z):
    M = (1<<2*Z+1)-1; D = [0]*(B+1); D[0] = 1<<Z
    for b in range(1, B+1):
        x = b; r = 0
        while x: u = x&-x; y = D[b^u]; v = W[u.bit_length()-1]; r |= ((y<<v)|(y>>v))&M; x ^= u
        D[b] = r
    return bool(D[B])
lo, hi = 0, max(W)
while lo < hi:
    if ok(mi:=(lo+hi)>>1): hi = mi
    else: lo = mi+1
print(lo)