from array import *
import sys; sys.set_int_max_str_digits(2*10**6)
N, X = map(int, input().split()); S = input(); V = array('i', [1]); U = set(); M = 1<<20
while V[-1] not in U: U.add(V[-1]); V.append((V[-1]*33+1)%M)
C = array('i', [0])
for i in range(X): C[0] += V[X*i%M]; C[0] %= M
for _ in range(X-1): C.append((33*C[-1]+X)%M)

A = int(''.join(map(str, C))); D = 1
while 27**D < A: D *= 2

W = array('b', [0]*D); Q = [(A, 0, D-1)]; Z = []
while Q:
    x, l, r = Q.pop()
    if x < 27: W[l] = x
    # divmod is faster than the regular // and %
    else: k = r-(l+r)//2; p, q = divmod(x, 27**k); Q.append((q, l, l+k-1)); Q.append((p, l+k, r))
while W[-1] == 0: W.pop()

for i in S:
    t = ord(i)-65
    if t < 0: t = 26
    t += W.pop(); t %= 27
    if t == 26: Z.append(' ')
    else: Z.append(chr(t+65))
sys.stdout.write(''.join(Z))