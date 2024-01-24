from array import *; import sys; input = sys.stdin.readline
for _ in range(int(input())):
    m, c, ii = map(int, input().split()); idx = ipos = ptr = 0; M = array('i', [0]*m); C = input().strip(); I = [*map(ord, input().strip()), 255]; R = {}; S = []; T = 0; L = []
    for i in range(c):
        if C[i] == '[': S.append(i)
        elif C[i] == ']': R[i] = S[-1]+1; R[S.pop()] = i+1
    while ptr < c and T < 50_000_000:
        if (x:=C[ptr]) == '-':   M[idx] = (M[idx]-1)%256
        elif x == '+': M[idx] = (M[idx]+1)%256
        elif x == '<': idx = (idx-1)%m
        elif x == '>': idx = (idx+1)%m
        elif x == ',': M[idx] = I[min(ipos, ii)]; ipos += 1
        elif x == '[':
            if M[idx] == 0: ptr = R[ptr]-1
            else: L.append((ptr, R[ptr]-1))
        elif x == ']':
            if M[idx]: ptr = R[ptr]-1
            else: L.pop()
        ptr += 1; T += 1
    if ptr >= c: print('Terminates')
    else: print('Loops', *L[0])