import sys; input = sys.stdin.readline
from array import *
def bt(idx, va, vb):
    if idx == m: return 1
    if asg[b[idx][0]] != -1 and asg[b[idx][0]] != va: return 0
    if asg[b[idx][1]] != -1 and asg[b[idx][1]] != vb: return 0
    if asg[b[idx][0]^1] != -1 and asg[b[idx][0]^1] == va: return 0
    if asg[b[idx][1]^1] != -1 and asg[b[idx][1]^1] == vb: return 0
    oa, ob = asg[b[idx][0]], asg[b[idx][1]]
    oax, obx = asg[b[idx][0]^1], asg[b[idx][1]^1]
    asg[b[idx][0]] = va; asg[b[idx][1]] = vb
    asg[b[idx][0]^1] = 1-va; asg[b[idx][1]^1] = 1-vb
    if bt(idx+1, 0, 1) or bt(idx+1, 1, 0) or bt(idx+1, 1, 1): return 1
    asg[b[idx][0]] = oa; asg[b[idx][1]] = ob
    asg[b[idx][0]^1] = oax; asg[b[idx][1]^1] = obx
    return 0
while True:
    try: n, m = map(int, input().split())
    except: break
    b = []
    for _ in range(m):
        p, q = input().strip().split()
        ip, jp = p[:-1], p[-1]; iq, jq = q[:-1], q[-1]
        ip, iq = int(ip), int(iq)
        xp = (jp < 'w'); xq = (jq < 'w')
        pp, qq = 4*ip+2*xp, 4*iq+2*xq; b.append((pp//2, qq//2))
    asg = array('i', [-1]*2*n)
    if not n: continue
    asg[0] = 1; asg[1] = 0
    ok = bt(0, 1, 0) or bt(0, 0, 1) or bt(0, 1, 1)
    if ok:
        for i in range(n):
            if asg[2*i] == -1: asg[2*i] = 1; asg[2*i+1] = 0
        print(*[f'{i//2}{"wh"[i%2]}' for i in range(2, 2*n) if asg[i] == asg[0]])
    else: print('bad luck')