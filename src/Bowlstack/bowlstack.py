from itertools import *

def f(h, r, R, hp, rp, Rp):
    if R <= rp:
        # completely on top of the other
        return 1, h
    elif Rp <= R and hp/(Rp-rp) <= h/(R-r) and hp <= (Rp-r)*h/(R-r):
        # similar to case 2, bowl 1 and bowl 2
        return 2, (Rp-r)*h/(R-r)-hp
    elif r <= rp <= R and hp/(Rp-rp) >= h/(R-r):
        # similar to case 1
        return 3, (rp-r)*h/(R-r)
    elif Rp >= R >= rp and hp/(Rp-rp) <= h/(R-r) and hp*(R-rp)/(Rp-rp) <= h:
        # similar to case 2, bowl 2 and bowl 3
        return 4, h-hp+(Rp-R)*hp/(Rp-rp)
    elif rp <= r:
        # top bowl touches the bottom bowl's base
        return 5, 0
    else:
        # should not happen
        assert 0, (h, r, R, hp, rp, Rp)

for _ in range(int(input())):
    N = int(input()); Q = [[*map(int, input().split())] for _ in range(N)]; B = 1e9
    for P in permutations(Q):
        H = [0]*N; M = 0
        for i in range(N):
            # consider P[i] as the top of the stack
            hp, rp, Rp = P[i]
            for j in range(i):
                h, r, R = P[j]
                _, dh = f(h, r, R, hp, rp, Rp)
                H[i] = max(H[i], H[j]+dh)
            M = max(M, H[i]+hp)
            if M > B: break
        B = min(B, int(M))
    print(B)