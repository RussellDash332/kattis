from math import *
L = input(); S = len(L)-1
if L == '0': print(0), exit(0)
for D in range(S+1, max(0, S-7), -1):
    lb = int(log10(D)+(D-1))
    if lb < S or (lb == S and str(D)+'0'*(D-1) <= L):
        ub = int(log10(D+1)+D)
        if ub > S or (ub == S and str(D+1)+'0'*D >= L):
            L = [*map(int, L)]; val = 0; start = 0
            for i in range(len(L)): # long division
                val *= 10; val += L[i]
                if val >= D: start = D
                if start: L[i] = val//D; val %= D
            print(''.join(map(str, L[-D:]))), exit(0)