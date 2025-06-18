from math import*;r,s,h=map(int,input().split());c=2*pi*r;d=c/h/s;b=(1,0,0,0)
for A in range(2,M:=1001):
 for B in range(2*A,M,A):
  for C in range(2*B,M,B):u=1/A-1/B+1/C;b=min(b,(min(abs(d-floor(d)-u),abs(d-ceil(d)+u)),A,B,C))
print(*b[1:])