from functools import*;I=lambda:[*map(int,input().split())];C,M=I();P=[I()for _ in'.'*M]
@cache
def f(m,c):
 if m<0:return 0
 else:return max([f(m-1,c),*(f(m-1,c-k)+P[m][k-1]for k in range(1,c+1))])
print(f(M-1,C))