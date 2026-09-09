def cross(a, b):
    return (a.conjugate()*b).imag
def intersect(a, b, c, d):
    return a+cross(c-a, d-c)/cross(b-a, d-c)*(b-a)
def check(p1, p2, p3, p4):
    c1 = cross(p2-p1, p3-p1); c2 = cross(p2-p1, p4-p1)
    if (c1 < -1e-9 and c2 < -1e-9) or (c1 > 1e-9 and c2 > 1e-9): return 0
    c1 = cross(p4-p3, p1-p3); c2 = cross(p4-p3, p2-p3)
    if (c1 < -1e-9 and c2 < -1e-9) or (c1 > 1e-9 and c2 > 1e-9): return 0
    return 1
N, M = map(int, input().split())
P = [complex(*map(int, input().split())) for _ in range(N)]
L = []
for _ in range(M): c, ha, hb = input().split(); L += [(ord(c[0])-65, ord(c[1])-65, int(ha), int(hb))]
G = [0]*M
for i in range(M):
    ai, bi, hai, hbi = L[i]
    for j in range(i+1, M):
        aj, bj, haj, hbj = L[j]
        if {ai,bi}&{aj,bj}: continue
        if not check(P[ai], P[bi], P[aj], P[bj]): continue
        p = intersect(P[ai], P[bi], P[aj], P[bj]); ti = hai+abs(p-P[ai])/abs(P[bi]-P[ai])*(hbi-hai); tj = haj+abs(p-P[aj])/abs(P[bj]-P[aj])*(hbj-haj)
        if abs(ti-tj)<6-1e-9: G[i] |= 1<<j; G[j] |= 1<<i; print(chr(ai+65)+chr(bi+65), chr(aj+65)+chr(bj+65), 'too close')
print(max(b.bit_count() for b in range(1<<M) if all(G[j]&b==0 or b&(1<<j)==0 for j in range(M))), 'ziplines')