for k in range(1, 101):
    p = [*map(int, str(2**k))]; q = [0]*len(p)
    for i in range(m:=(len(p)+1)//2): q[i] = q[-i-1] = p[i]
    while p < q:
        while p < q and q[-m]: q[m-1] = q[-m] = q[-m]-1
        if p < q: q[-m] = q[m-1] = 9
        m -= 1
    print(k, ' ', *q, sep='')