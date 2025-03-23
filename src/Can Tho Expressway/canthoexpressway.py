import sys; input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c1, c2 = map(int, input().split()); k, *v = map(int, input().split()); P = [(v[2*i], v[2*i+1]) for i in range(k)]; V = []; Z = 0
    for i in range(k):
        x1, y1 = P[i]; x2, y2 = P[(i+1)%k]; v1 = a*x1+b*y1; v2 = a*x2+b*y2
        Z |= (v1-c1)*(v2-c1)<0 or (v1-c2)*(v2-c2)<0 # diff sides of the line
        Z |= (v1-c1)==(v2-c2)==0 or (v1-c2)==(v2-c1)==0 # each point on each line
        Z |= (v1-c1)*(v1-c2)<0 # point between both lines
    print('YNEOS'[1-Z::2])