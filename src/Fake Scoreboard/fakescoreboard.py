import sys; input = sys.stdin.readline
def can(rr, cc):
    C2 = [e*c+i for i, e in enumerate(C)]
    for i in range(rr, r):
        v = R[i]; C2 = sorted(x for x in C2 if x >= c); j = 0
        while j < len(C2) and v:
            if C2[-1-j]%c >= cc*(i==rr): C2[-1-j] -= c; v -= 1
            j += 1
        if v: return 0
    return not C2 or min(C2)//c == max(C2)//c == 0
while True:
    r, c = map(int, input().split())
    if r*c == 0: break
    R = [*map(int, input().split())]; C = [*map(int, input().split())]; input(); M = [[0]*c for _ in range(r)]
    if max(C) > r or max(R) > c or not can(0, 0): print('Impossible\n'); continue
    for i in range(r*c): v = 1-can((i+1)//c, (i+1)%c); M[i//c][i%c] = v; R[i//c] -= v; C[i%c] -= v
    sys.stdout.write('\n'.join(''.join('NY'[i] for i in x) for x in M)+'\n\n')