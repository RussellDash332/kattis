import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
B, H, N = map(int, input().split()); E = []; ys = set()
for _ in range(N): x1, x2, y1, y2 = map(int, input().split()); E.append((x1, 1, y1, y2)); E.append((x2, -1, y1, y2)); ys.add(y1); ys.add(y2)
ys = sorted(list(ys)); bm = {y:i for i,y in enumerate(ys)}; W = 1
while W < len(ys)-1: W <<= 1
C = array('i', [0]*(2*W)); S = array('i', [0]*(2*W)); TL = array('i', [0]*(2*W))
for i in range(len(ys)-1): TL[W+i] = ys[i+1]-ys[i]
for i in range(W-1, 0, -1): TL[i] = TL[2*i]+TL[2*i+1]
Z = B*H; px = E[0][0] if E else 0
for x, ty, y1, y2 in sorted(E, key=lambda x: x[0]):
    if x != px: Z -= (x-px)*S[1]; px = x
    ql = bm[y1]; qr = bm[y2]-1
    if ql > qr: continue
    l = ql+W; r = qr+W+1; l0 = l; r0 = r-1
    while l < r:
        if l & 1: C[l] += ty; S[l] = TL[l] if C[l] > 0 else (S[2*l]+S[2*l+1] if l < W else 0); l += 1
        if r & 1: r -= 1; C[r] += ty; S[r] = TL[r] if C[r] > 0 else (S[2*r]+S[2*r+1] if r < W else 0)
        l >>= 1; r >>= 1
    l = l0>>1; r = r0>>1
    while l > 0: S[l] = TL[l] if C[l] > 0 else (S[2*l]+S[2*l+1]); l >>= 1
    while r > 0: S[r] = TL[r] if C[r] > 0 else (S[2*r]+S[2*r+1]); r >>= 1
print(Z)