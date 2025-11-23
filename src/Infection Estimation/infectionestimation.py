S=10**7;from math import*;L=[l:=0]+[l:=l+log(i+1)for i in range(S)];N=len(C:=[int(100*1.01**i)for i in range(1088)]);D=[1/N]*N
def p(X,k):return 1-exp(L[S-X]+L[S-k]-L[S]-L[S-X-k])if X+k<=S else 1
for _ in'.'*50:
 l,h=1,S
 while h>l:
  m=(l+h)>>1
  if(s:=sum(p(C[i],m)*D[i]for i in range(N)))<.5:l=m+1
  else:h=m
 print('test',l);v=int(input())
 for i in range(N):x=p(C[i],l);D[i]*=[(1-x)/(1-s),x/s][v]
print('estimate',C[D.index(max(D))])