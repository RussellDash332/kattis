import sys
input()

def gen(n):
    res = [1]
    for i in range(n//2):
        c = res[-1]
        res.append(c*(n-i)//(i+1))
    rev = res[::-1]
    if n % 2 == 0: return res[:-1] + rev
    return res + rev

for line in sys.stdin:
    n, v1, v2, w = map(int, line.split())
    r = n-v1-v2
    # To recount, only this scenario is considered
    if v1+r<=v2: print('RECOUNT!')
    else:
        combs, s = gen(r), 0
        for i in range(r+1):
            if v1+i>v2+(r-i): s += combs[i]
        if 100*s > w*2**r: print('GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!')
        else: print('PATIENCE, EVERYONE!')