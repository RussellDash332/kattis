from bisect import *
class SortedList:
    def __init__(s, A=None, l1=200, l2=64, mv=~(1<<30)):
        s.l1 = l1; s.l2 = l2; s.x1 = s.l1*2; s.x2 = s.l2*2; s.g1 = len(bin(s.x1))-3; s.g2 = len(bin(s.x2))-3; s.mv = mv; s.clear()
        if not A: return
        s.cnt = len(A:=sorted(A))
        for l in range(0, s.cnt, s.l1): s.b.append(A[l:min(l+s.l1, s.cnt)])
        s._ex()
    def clear(s): s.b = [[]]; s.bc = [0]; s.bm = [0]; s.sm = []; s.ss = []; s.cnt = 0
    def __len__(s): return s.cnt
    def _ex(s):
        bo = [*s.b]; c = sum(map(bool, bo)); sn = (c+s.l2-1)//s.l2; ec = s.cnt; s.clear(); s.cnt = ec; s.sm.extend([s.mv]*sn); s.ss.extend([0]*sn); i = 0
        for bk in bo:
            if bk:
                s.sm[i>>s.g2-1] = bk[-1]; s.ss[i>>s.g2-1] += 1; s.bm.append(bk[-1]); s.bc.append(len(bk)); s.b.append(bk); i += 1
                if i&(s.l2-1) == 0 and i < c: s.b.extend([] for _ in range(s.l2)); s.bc.extend([0]*s.l2); s.bm.extend([0]*s.l2)
        for i in range(1, len(s.bc)):
            if i+(i&-i) < len(s.bc): s.bc[i+(i&-i)] += s.bc[i]
    def __getitem__(s, k):
        assert -s.cnt <= k < s.cnt; k %= s.cnt; bi = 0; i = 1<<(len(bin(len(s.bc)-1))-3)
        while i:
            if bi|i < len(s.bc) and k >= s.bc[bi|i]: k -= s.bc[bi:=bi|i]
            i >>= 1
        return s.b[bi+1][k]
    def _lb(s, x):
        if not s.ss: return (0, len(s.b[0]))
        l = -1; r = len(s.ss)-1
        while r-l > 1:
            if s.sm[m:=(l+r)>>1] >= x: r = m
            else: l = m
        l = r<<s.g2; r = r<<s.g2|s.ss[r]
        while r-l > 1:
            if s.bm[m:=(l+r)>>1] >= x: r = m
            else: l = m
        return (r, bisect_left(s.b[r], x))
    def _ub(s, x):
        if not s.ss: return (0, len(s.b[0]))
        l = -1; r = len(s.ss)-1
        while r-l > 1:
            if s.sm[m:=(l+r)>>1] >= x: r = m
            else: l = m
        l = r<<s.g2; r = r<<s.g2|s.ss[r]
        while r-l > 1:
            if s.bm[m:=(l+r)>>1] >= x: r = m
            else: l = m
        return (r, bisect(s.b[r], x))
    def _rbm(s, b1, b2):
        for i in range(b1, b2+1): s.bc[i] = 0
        for i in range(b1, b2+1):
            if s.b[i]: s.bc[i] += len(s.b[i]); s.bm[i] = s.b[i][-1]
            if i+(i&-i) <= b2: s.bc[i+(i&-i)] += s.bc[i]
        lo = (-b2&b2)//2
        while lo >= s.x2: s.bc[b2] += s.bc[b2-lo]; lo >>= 1
    def index(s, x):
        if not s.ss: return 0
        bi, rk = s._lb(x); i = bi-1
        while i: rk += s.bc[i]; i ^= i&-i
        return rk
    def append(s, x):
        s.cnt += 1
        if not s.ss: s.b.append([x]); s.bc.append(1); s.bm.append(x); s.sm.append(x); s.ss.append(1); return
        bi, it = s._lb(x); i = bi
        while i < len(s.bc): s.bc[i] += 1; i += i&-i
        s.b[bi].insert(it, x); si = (bi-1)>>s.g2; s.bm[bi] = max(s.bm[bi], x); s.sm[si] = max(s.sm[si], x)
        if len(s.b[bi]) >= s.x1:
            bj = (si<<s.g2)|s.ss[si]; bn = si+1<<s.g2
            if len(s.b) <= bn: s.b.insert(bi+1, s.b[bi][s.l1:]); s.bc.append(0); s.bm.append(0)
            else: s.b[bi+2:bj+2] = s.b[bi+1:bj+1]; s.b[bi+1] = s.b[bi][s.l1:]
            s.b[bi] = s.b[bi][:s.l1]; s.ss[si] += 1
            if s.ss[si] == s.x2: s._ex()
            else: s._rbm(si<<s.g2|1, min(bn, len(s.bc)-1))
    def remove(s, x):
        if not s.sm or s.sm[-1] < x: return
        bi, it = s._lb(x)
        if it == len(s.b[bi]) or s.b[bi][it] > x: return
        s.cnt -= 1; i = bi
        while i < len(s.bc): s.bc[i] -= 1; i += i&-i
        s.b[bi].pop(it); si = (bi-1)>>s.g2; bj = (si<<s.g2)|s.ss[si]
        if s.b[bi]:
            s.bm[bi] = s.b[bi][-1]
            if bi == bj: s.sm[si] = s.b[bi][-1]
        else:
            if len(s.b) <= (bn:=si+1<<s.g2):
                s.b.pop(bi); s.bm.pop(bi); s.bc.pop(); s.ss[si] -= 1
                if s.ss[si] == 0: s.sm.pop(); s.ss.pop()
                else:
                    s._rbm(si<<s.g2|1, len(s.bc)-1)
                    if bi == bj: s.sm[si] = s.b[bj-1][-1]
            else:
                s.ss[si] -= 1
                if s.ss[si] == 0: s._ex()
                else:
                    s.b[bi:bj] = s.b[bi+1:bj+1]; s.b[bj] = []; s._rbm(si<<s.g2|1, bn)
                    if bi == bj: s.sm[si] = s.b[bj-1][-1]
    def pop(s, k=-1): s.remove(v:=s[k]); return v
import sys; input = sys.stdin.readline; from array import *
n,k=map(int,input().split());w=[input()for _ in'.'*n];p=array('i',(int(input())for _ in'.'*k));z=0;W=SortedList(range(n))
for i in range(n-1):W.pop(z:=(z+p[i%k])%(n-i))
print(w[W[0]])