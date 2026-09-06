from functools import*;input();N=len(s:=input());M=len(t:=input())
@cache
def f(i,j):
 if i<1:return j<1
 for k in range(1,min(i,j)+1):
  for p in range(k,j+1,k):
   if s[i-k:i]==t[j-p:j-p+k]:
    if f(i-k,j-p):return 1
   else:break
 return f(i-1,j)
print('yneos'[1-f(N,M)::2])