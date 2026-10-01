from functools import*;K=int(input());N=int(input());P=[[*map(int,input().split())]for _ in'.'*N]
@cache
def f(n,*t):
 if n==N:return 0
 t=[*t];z=f(n+1,*t);k,A,B=P[n]
 for i in range(4):
  if t[i]>=k:t[i]-=k;z=max(z,f(n+1,*t)+A+B*-~i);t[i]+=k
 return z
print(f(0,*[K]*4))