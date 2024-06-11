n = [*map(int, input())]; H = [0]*800; lo = -1
for i in range(len(n)):
    if n[i] < lo:
        for j in range(i+1, len(n)):
            if n[j] > n[j-1]: print(-1), exit(0)
    lo = n[i]
def dp(p, d, l, z):
    if d == len(n): return 1
    if H[(t:=80*p+4*d+2*l+z)]: return H[t]
    for i in range(min((n[d], 9)[z], (9, p)[l])+1): H[t] += dp(i, d+1, l or i<p, z or i!=n[d])
    return H[t]
print(dp(0, 0, 0, 0)-1)