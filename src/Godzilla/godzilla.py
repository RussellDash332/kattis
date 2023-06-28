import sys
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

def check():
    clear = True
    for rr in range(gr-1, -1, -1):
        if rs[rr*c+gc] > d: clear = False; break
        if rr*c+gc in vm and clear: return True
    clear = True
    for rr in range(gr+1, r):
        if rs[rr*c+gc] > d: clear = False; break
        if rr*c+gc in vm and clear: return True
    clear = True
    for cc in range(gc-1, -1, -1):
        if rs[gr*c+cc] > d: clear = False; break
        if gr*c+cc in vm and clear: return True
    clear = True
    for cc in range(gc+1, c):
        if rs[gr*c+cc] > d: clear = False; break
        if gr*c+cc in vm and clear: return True
    return False

input()
c = r = 0
for line in sys.stdin:
    if c + r == 0:
        c, r = map(int, line.split())
        N = r*c
        vm, rs = set(), [-1]*(r*c)
        xr, m = r, []
    elif xr:
        m.append(list(line.strip()))
        xr -= 1
        if xr == 0:
            for i in range(r):
                for j in range(c):
                    if m[i][j] == 'G': gr, gc = i, j
                    elif m[i][j] == 'M': vm.add(i*c+j)
                    elif m[i][j] == 'R': rs[i*c+j] = 1e9
            vg, d, q = {gr*c+gc}, 1, list(vm)
            while True:
                # next step for Godzilla
                fd = 1
                for dr, dc in delta: # try to break a house
                    new = (gr+dr)*c + (gc+dc)
                    if 0 <= gr+dr < r and 0 <= gc+dc < c and new not in vg and rs[new] == 1e9: vg.add(new); gr, gc = gr+dr, gc+dc; fd = 0; rs[new] = d; break
                if fd:
                    for dr, dc in delta:
                        new = (gr+dr)*c + (gc+dc)
                        if 0 <= gr+dr < r and 0 <= gc+dc < c and new not in vg: vg.add(new); gr, gc = gr+dr, gc+dc; break
                # move the mechs
                q2 = []
                for u in q:
                    ur, uc = u//c, u%c
                    for dr, dc in delta:
                        new = (ur+dr)*c + (uc+dc)
                        if 0 <= ur+dr < r and 0 <= uc+dc < c and new not in vm and rs[new] <= d: vm.add(new), q2.append(new)
                if check(): break
                q = q2
                d += 1
            print(sum(1 for i in rs if -1 < i <= d))
            r = c = 0