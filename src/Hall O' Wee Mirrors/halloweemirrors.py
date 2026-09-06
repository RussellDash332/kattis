def proj(p, a, b):
    return a+((p-a)/(b-a)).real*(b-a)
def valid(z, p, q):
    return min(p.real, q.real)-1e-9 <= z.real <= max(p.real, q.real)+1e-9 and min(p.imag, q.imag)-1e-9 <= z.imag <= max(p.imag, q.imag)+1e-9
while (n:=int(input())):
    M = []
    for _ in range(n): x1, y1, x2, y2 = map(int, input().split()); M += [(x1+y1*1j, x2+y2*1j)]
    for _ in range(int(input())):
        p = complex(*map(int, input().split())); z = 0
        for a, b in M: z += valid(proj(p, a, b), a, b)
        print(z)
    print()