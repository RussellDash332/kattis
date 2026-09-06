def proj(p, a, b):
    return a+((p-a)/(b-a)).real*(b-a)
def valid(z, p, q):
    return min(p.real, q.real)-1e-9 <= z.real <= max(p.real, q.real)+1e-9 and min(p.imag, q.imag)-1e-9 <= z.imag <= max(p.imag, q.imag)+1e-9
n, d = map(eval, input().split())
P = []
for _ in range(n):
    x, y, *r = map(float, input().split())
    P += [(x+y*1j, r)]
s = complex(*map(float, input().split())); Z = []
for p, r in P:
    if r and abs(s-p)<r[0]-1e-9: print('no'); exit()
for i in range(n):
    t = (P[i][0], P[i-1][0]); v = abs(t[0]-t[1]); z = proj(s, t[0], t[1])
    r = P[i][1][0] if P[i][1] else 0; Z += [t[0]+r/v*(t[1]-t[0])]
    r = P[i-1][1][0] if P[i-1][1] else 0; Z += [t[1]+r/v*(t[0]-t[1])]
    if valid(z, t[0], t[1]): Z += [z]
print('yneos'[min(abs(i-s) for i in Z if all(abs(p-i)>=r[0]-1e-9 for p, r in P if r))>d+1e-9::2])