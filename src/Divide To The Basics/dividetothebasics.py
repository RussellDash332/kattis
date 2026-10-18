from functools import*
@cache
def f(N):
 z=1
 for p in range(2,int(N**.5)+1):
  if N%p<1:z+=f(p)+f(N//p)*(p*p<N)
 return z
print(f(int(input()))%(10**9+7))