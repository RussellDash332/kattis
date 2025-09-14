from functools import*;N=int(input());R=int(input());C={};M={}
for _ in'.'*R:c,k=input().split();C[c]=int(k)
def f(n,d):
 if n==N:return 1
 K=(n,tuple(d.items()))
 if K in M:return M[K]
 z=(36-R)*f(n+1,d)
 for i in C:
  if d[i]<C[i]:d[i]+=1;z+=f(n+1,d);d[i]-=1
 M[K]=z;return z
print(f(0,{c:0for c in C}))