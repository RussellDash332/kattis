import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
L = array('i'); R = array('i'); LC = array('i'); RC = array('i'); MN = array('i'); Z = array('i'); NM = array('i'); NE = array('i')
def make(l, r): L.append(l); R.append(r); LC.append(-1); RC.append(-1); MN.append(0); Z.append(0); NM.append(r-l+1); NE.append(NM[-1]); return len(L)-1
M = 10**9; E = []; make(-M, M); px = -M; ZZ = 0; st = []
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    E.append((x1, y1, y2-1, 1)); E.append((x2, y1, y2-1, -1))
for x, s, e, v in sorted(E, key=lambda x: x[0]):
    if x != px: ZZ += (x-px)*(NE[0]-NM[0]); px = x
    st.append(0)
    while st:
        i, b = divmod(st.pop(), 2); l = LC[i]; r = RC[i]
        if b:
            if MN[l] == MN[r]: NM[i] = NM[l]+NM[r]; MN[i] = MN[l]
            elif MN[l] > MN[r]: NM[i] = NM[r]; MN[i] = MN[r]
            else: NM[i] = NM[l]; MN[i] = MN[l]
            NE[i] = NE[l]+NE[r]; continue
        if L[i] > e or R[i] < s: continue
        if L[i] >= s and R[i] <= e:
            if v%2: NE[i] = R[i]-L[i]+1-NE[i]
            MN[i] += v; Z[i] += v; continue
        if L[i] < R[i]:
            if l == -1: l = LC[i] = make(L[i], m:=(L[i]+R[i])>>1); r = RC[i] = make(m+1, R[i])
            if Z[i]:
                MN[l] += Z[i]; Z[l] += Z[i]; MN[r] += Z[i]; Z[r] += Z[i]
                if Z[i]%2: NE[l] = R[l]-L[l]+1-NE[l]; NE[r] = R[r]-L[r]+1-NE[r]
                Z[i] = 0
        st.append(2*i+1); st.append(2*l); st.append(2*r)
print(ZZ)