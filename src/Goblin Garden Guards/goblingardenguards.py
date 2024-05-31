import sys; input = sys.stdin.readline; from array import *; M = 10201; g = [0]*M*M; p = sorted((i*i+j*j,i,j) for i in range(-100, 101) for j in range(-100, 101) if i*i+j*j<=10**4); X = array('B', [k[1]+100 for k in p]); Y = array('B', [k[2]+100 for k in p]); l = array('h'); c = 0
for i in range(len(p)):
    if (X[i]-100)**2+(Y[i]-100)**2>c*c: l.append(i); c += 1
l.append(len(p))
for _ in range(int(input())): x, y = map(int, input().split()); g[M*(x+100)+(y+100)] += 1
for _ in range(int(input())):
    x, y, r = map(int, input().split())
    for i in range(l[r]): g[M*(x+X[i])+y+Y[i]] = 0
print(sum(g))