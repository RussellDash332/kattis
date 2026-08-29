def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
n, d = map(float, input().split()); Z = 0
cx, cy, cz = cross([*map(float, input().split())], [*map(float, input().split())])
for _ in range(round(n)):
    px, py, pz = map(float, input().split())
    vx, vy, vz = map(float, input().split())
    px -= d*vx; py -= d*vy; pz -= d*vz
    Z += abs(px*cx+py*cy+pz*cz) < 1e-8
print(Z)