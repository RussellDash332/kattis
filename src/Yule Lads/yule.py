from array import *
N = int(input()); Z = 0
L = int(N**.5+2); M = array('i', [1]*L)
for i in range(2, int(L**.5)+1):
    if M[i] == 1:
        for j in range(i, L, i): M[j] *= -i
        for j in range(i*i, L, i*i): M[j] = 0
for i in range(2, L):
    if M[i] == i: M[i] = 1
    elif M[i] == -i: M[i] = -1
    elif M[i] < 0: M[i] = 1
    elif M[i] > 0: M[i] = -1
for i in range(1, L):
    if i*i > N: break
    Z += N//i//i*M[i]
print(Z)