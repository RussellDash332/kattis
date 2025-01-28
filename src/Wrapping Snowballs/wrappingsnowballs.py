from math import*;R,N,*A=map(int,open(0).read().split())
for r in A:print(2*pi*R*R*(1-cos(min(r/R,pi))))