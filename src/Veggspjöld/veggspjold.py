# Partial 95 points :)
import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
L = array('i'); R = array('i'); LC = array('i'); RC = array('i'); MN = array('i'); Z = array('i'); NM = array('i'); NE = array('i')
def make(l, r): L.append(l); R.append(r); LC.append(-1); RC.append(-1); MN.append(0); Z.append(0); NM.append(r-l+1); NE.append(NM[-1]); return len(L)-1
B, H, N = map(int, input().split()); M = 10**9; E = []; make(0, M); px = -M; ZZ = B*H; st = array('i')
for _ in range(N): x1, x2, y1, y2 = map(int, input().split()); E.append((x1, y1, y2-1, 1)); E.append((x2, y1, y2-1, -1))
for x, s, e, v in sorted(E, key=lambda x: x[0]):
    if x != px: ZZ -= (x-px)*(NE[0]-NM[0]); px = x
    st.append(0)
    while st:
        i, b = divmod(st.pop(), 2); l = LC[i]; r = RC[i]
        if b:
            if MN[l] == MN[r]: NM[i] = NM[l]+NM[r]; MN[i] = MN[l]
            elif MN[l] > MN[r]: NM[i] = NM[r]; MN[i] = MN[r]
            else: NM[i] = NM[l]; MN[i] = MN[l]
            continue
        if L[i] > e or R[i] < s: continue
        if L[i] >= s and R[i] <= e: MN[i] += v; Z[i] += v; continue
        if L[i] < R[i]:
            if l == -1: l = LC[i] = make(L[i], m:=(L[i]+R[i])>>1); r = RC[i] = make(m+1, R[i])
            if Z[i]: MN[l] += Z[i]; Z[l] += Z[i]; MN[r] += Z[i]; Z[r] += Z[i]; Z[i] = 0
        st.append(2*i+1); st.append(2*l); st.append(2*r)
print(ZZ)