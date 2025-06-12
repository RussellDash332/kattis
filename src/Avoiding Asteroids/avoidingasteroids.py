def dist(a, b, c): return (a*a+b*b+c*c)**0.5
def dot(a, b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross_util(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def cross(a, b, c): return cross_util((b[0]-a[0], b[1]-a[1], b[2]-a[2]), (c[0]-a[0], c[1]-a[1], c[2]-a[2]))
def perp_dist(p, s):
    a, b = s
    if dot((a[0]-p[0], a[1]-p[1], a[2]-p[2]), (a[0]-b[0], a[1]-b[1], a[2]-b[2])) <= 0: return dist(a[0]-p[0], a[1]-p[1], a[2]-p[2])
    if dot((b[0]-p[0], b[1]-p[1], b[2]-p[2]), (b[0]-a[0], b[1]-a[1], b[2]-a[2])) <= 0: return dist(b[0]-p[0], b[1]-p[1], b[2]-p[2])
    return dist(*cross(p, a, b))/dist(a[0]-b[0], a[1]-b[1], a[2]-b[2])
sx, sy, sz, bx, by, bz, n = map(eval, input().split()); L = 10**8
for _ in range(n):
    px, py, pz, dx, dy, dz, m = map(eval, input().split()); d = dist(dx, dy, dz)
    v = [*map(float, input().split())]; r = max(dist(v[3*i]-px, v[3*i+1]-py, v[3*i+2]-pz) for i in range(m))
    S, E = (px, py, pz), (px+dx/d*L, py+dy/d*L, pz+dz/d*L)
    def f(k): return perp_dist((px+dx*k, py+dy*k, pz+dz*k), ((sx, sy, sz), (bx, by, bz)))
    a, b = 0, L/d; gr = (5**0.5-1)/2
    for _ in range(42):
        if f(μ:=(1-gr)*a+gr*b) > f(λ:=gr*a+(1-gr)*b): b = μ
        else: a = λ
    if f((a+b)/2) <= r: print('Surrender'); exit()
print('Go')