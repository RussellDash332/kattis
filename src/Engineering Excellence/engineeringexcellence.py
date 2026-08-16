from cmath import *
def cross(a, b):
    return (a.conjugate()*b).imag
def dot(a, b):
    return (a*b.conjugate()).real
def intersect(l1, l2):
    (s1, e1), (s2, e2) = l1, l2; t = cross(s2-s1, q:=e2-s2)
    if (d:=cross(e1-s1, q)) == 0: return None
    t /= d; return s1*(1-t)+e1*t
N = int(input()); E = exp(pi*.5j); Z = 0; eps = 1e-5
P = [complex(*map(int, input().split())) for _ in range(N)]
for i in range(N):
    a, b, c, d, e = (P[(i+j)%N] for j in range(-2, 3)); m = (b+d)/2; n1 = (e-d)*E; n2 = (b-a)*E; n3 = d-e; n4 = b-a; q = abs(c-d)+abs(c-b)
    def valid(p): return p != None and dot(p-e, n1)>=-eps<=dot(p-a, n2) and dot(p-d, n3)>=-eps<=dot(p-b, n4) and abs(p-m)<=abs(b-m)+eps and (phase(p-m)-phase(b-m))%(2*pi) <= pi
    z = [m+(d-m)/E]
    for x in (1, E):
        for u, v in (((d-e)/x, d), ((b-a)/x, b)):
            u2 = abs(u)**2
            if u2 and dot((y:=v-2*dot(u, v-m)*u/u2)-m, (b-d)*1j) >= -eps: z += [y]
        for y in (1, E): z += [intersect((d+(e-d)*x, d), (b+(a-b)*y, b))]
    for p in z:
        if valid(p): Z = max(Z, abs(p-d)+abs(p-b)-q)
print(Z)