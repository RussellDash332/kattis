import sys; input = sys.stdin.readline; from array import *
for _ in range(int(input())):
    N = int(input()); A = array('i', map(int, input().split())); S = [N]; Z = 1; L = array('i', [-1]*N); R = array('i', [N]*N); H = {}
    for i in range(N):
        if A[i] not in H: H[A[i]] = []
        H[A[i]].append(i)
    for h in H.values():
        for i in range(len(h)-1): L[h[i+1]] = h[i]; R[h[i]] = h[i+1]
    while S:
        l, r = divmod(S.pop(), N+1); h = 1
        if l >= r-1: continue
        ll = l; rr = r-1
        for _ in range(r-l):
            if L[ll] < l and R[ll] >= r: S.append((N+1)*l+ll); S.append((N+1)*(ll+1)+r); h = 0; break
            if L[rr] < l and R[rr] >= r: S.append((N+1)*l+rr); S.append((N+1)*(rr+1)+r); h = 0; break
            ll += 1; rr -= 1
        if h: Z = 0; break
    sys.stdout.write('non-'*Z+'boring\n')