import sys; input = sys.stdin.readline; from random import *; from array import *; M = 10**9+7; M2 = 10**9-63; P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
for _ in range(int(input())):
    A = input().strip(); B = input().strip(); fa = array('i', [1]); fb = array('i', [1]); ga = array('i', [1]); gb = array('i', [1]); N = len(A); Z = None; shuffle(P)
    for i in A: p = P[ord(i)-97]; fa.append(fa[-1]*p%M); ga.append(ga[-1]*p%M2)
    for i in B: p = P[ord(i)-97]; fb.append(fb[-1]*p%M); gb.append(gb[-1]*p%M2)
    ifa = array('i', [pow(i, -1, M) for i in fa]); ifb = array('i', [pow(i, -1, M) for i in fb]); iga = array('i', [pow(i, -1, M2) for i in ga]); igb = array('i', [pow(i, -1, M2) for i in gb]); H = {(fb[i]*ifb[j]%M , gb[i]*igb[j]%M2)for i in range(1, N+1) for j in range(i)}
    for l in range(N, 0, -1):
        for i in range(N+1-l):
            if (fa[i+l]*ifa[i]%M, ga[i+l]*iga[i]%M2) in H: Z = A[i:i+l]; break
        if Z != None: break
    print(Z or 'NONE')