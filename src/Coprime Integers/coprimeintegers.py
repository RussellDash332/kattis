from array import *
a, b, c, d = map(int, input().split()); L = max(b, d)+1; S = (b-a+1)*(d-c+1); M = array('i', [1]*L)
for i in range(2, int(L**.5)+1):
    if M[i] == 1:
        for j in range(i, L, i): M[j] *= -i
        for j in range(i*i, L, i*i): M[j] = 0
for i in range(2, L):
    if M[i] == i: M[i] = 1
    elif M[i] == -i: M[i] = -1
    elif M[i] < 0: M[i] = 1
    elif M[i] > 0: M[i] = -1
for n in range(2, L): S += M[n]*((b//n-(a-1)//n)*(d//n-(c-1)//n))
print(S)