for _ in range(int(input())):
    n, m = map(int, input().split()); z = []; t = 0; s = 1
    while 3*t+1 <= n: z += [(1, s+1), (2*s, 3*s-1)]; t = 3*t+1; s = 3*s-1
    j = n-t; z += [(s-j//2+(1-j%2), s+1), (2*s, 2*s+j//2)]; lo, hi = 1, max(map(max, z))
    while lo < hi:
        mi = (lo+hi)//2; s = 0
        for a, b in z: s += min(b, mi)-min(a, mi)
        if s >= m: hi = mi
        else: lo = mi+1
    print(lo-1)