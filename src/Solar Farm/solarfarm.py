def g(x):
    lo, hi = 0, int((4*r*r-x*x*w*w)**.5/h)+1
    while lo < hi:
        y = (lo+hi)//2
        if x*x*w*w + y*y*h*h > 4*r*r: hi = y
        else: lo = y+1
    return x*(lo-1)
for _ in range(int(input())):
    r, w, h = map(int, input().split())
    if w < h: w, h = h, w
    K = int(2**.5*r/w); print(max(map(g, range(max(K-250, 0), min(K+250, 2*r//w+1)))))