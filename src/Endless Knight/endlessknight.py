MOD = 10007
fact = [1, 1]
for i in range(MOD): fact.append(fact[-1]*(i+2)%MOD)
def binmod(n, r):
    if r > n: return 0
    if r == 0 or r == n: return 1
    if n < MOD: return fact[n]*pow(fact[r]*fact[n-r], -1, MOD)%MOD
    else:
        s = 1
        while n: s = s*binmod(n%MOD, r%MOD)%MOD; n //= MOD; r //= MOD
        return s

for tc in range(int(input())):
    h, w, r = map(int, input().split()); h -= 1; w -= 1
    rocks = []
    for _ in range(r):
        x, y = map(int, input().split()); x -= 1; y -= 1
        if (2*x-y)%3 or (2*y-x)%3 or 2*x<y or 2*y<x: continue
        rocks.append(((2*x-y)//3, (2*y-x)//3))
    if (2*h-w)%3 or (2*w-h)%3 or 2*h<w or 2*w<h: print(f'Case #{tc+1}: 0'); continue
    h, w = (2*h-w)//3, (2*w-h)//3
    rocks2 = []
    for x, y in rocks:
        if 0<=x<=h and 0<=y<=w: rocks2.append((x, y))
    rocks = sorted(rocks2); ans = 0
    for i in range(1<<len(rocks)):
        rr = [(0, 0)]
        for j in range(len(rocks)):
            if i&(1<<j): rr.append(rocks[j])
        rr.append((h, w))
        ways = 1
        for i in range(1, len(rr)):
            dr = rr[i][0]-rr[i-1][0]
            dc = rr[i][1]-rr[i-1][1]
            ways *= binmod(dr+dc, dr)
        ans += (-1)**(len(rr)%2)*ways; ans %= MOD
    print(f'Case #{tc+1}:', ans)