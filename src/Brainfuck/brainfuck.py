from array import *
m = 50000; idx = ptr = 0; M = array('B', [0]*m); C = ''.join(i for i in open(0).read() if i in '<>+-.[]'); R = {}; S = []; Z = []
for i in range(len(C)):
    if C[i] == '[': S.append(i)
    elif C[i] == ']': R[i] = S[-1]; R[S.pop()] = i
while ptr < len(C):
    if (x:=C[ptr]) == '-': M[idx] = (M[idx]-1)%256
    elif x == '+': M[idx] = (M[idx]+1)%256
    elif x == '<': idx = (idx-1)%m
    elif x == '>': idx = (idx+1)%m
    elif x == '[':
        if M[idx] == 0: ptr = R[ptr]
    elif x == ']':
        if M[idx]: ptr = R[ptr]
    else: Z.append(chr(M[idx]))
    ptr += 1
print(''.join(Z))