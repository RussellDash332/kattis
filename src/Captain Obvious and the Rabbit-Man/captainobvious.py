import sys

# FFT suffers precision issues so let's not use that
def mult(p1, p2, M):
    coef = [0]*(len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)): coef[i+j] = (coef[i+j] + p1[i]*p2[j]) % M
    return coef

input()
tog = 1
for line in sys.stdin:
    if tog: k, M = map(int, line.split())
    else:
        a = list(map(int, line.split()))
        fibs = [1, 2]
        for _ in range(k-2): fibs.append((fibs[-1] + fibs[-2]) % M)
        if k < 3: fibs = fibs[:k]
        polys = [[-i, 1] for i in fibs]
        while len(polys) != 1:
            new_polys = []
            for i in range(len(polys)//2): new_polys.append(mult(polys[2*i], polys[2*i+1], M))
            if len(polys) % 2: new_polys.append(polys[-1])
            polys = new_polys
        print(-sum(x*y for x,y in zip(polys[0], a)) % M)
    tog = 1-tog