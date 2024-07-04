import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
L = array('i'); R = array('i'); LC = array('i'); RC = array('i'); Z = array('i'); NE = array('i')
def make(l, r): L.append(l); R.append(r); LC.append(-1); RC.append(-1); Z.append(0); NE.append(r-l+1); return len(L)-1
def add(i, v):
    Z[i] += v
    if v%2: NE[i] = R[i]-L[i]+1-NE[i]
M = 10**9; E = []; make(-M, M); st = []; pe = NE[0]
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    E.append((x1, y1, y2-1, 1)); E.append((x2, y1, y2-1, -1))
for x, s, e, v in sorted(E, key=lambda x: x[0]):
    st.append(0)
    while st:
        i, b = divmod(st.pop(), 2); l = LC[i]; r = RC[i]
        if b: NE[i] = NE[l]+NE[r]; continue
        if L[i] > e or R[i] < s: continue
        if L[i] >= s and R[i] <= e: add(i, v); continue
        if L[i] < R[i]:
            if l == -1: LC[i] = make(L[i], m:=(L[i]+R[i])>>1); RC[i] = make(m+1, R[i])
            if Z[i]: add(LC[i], Z[i]); add(RC[i], Z[i]); Z[i] = 0
        st.append(2*i+1); st.append(2*LC[i]); st.append(2*RC[i])
    if e-s+1 != abs(pe-(pe:=NE[0])): print(1), exit(0)
print(0)