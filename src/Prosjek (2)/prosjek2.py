from array import*;import os,io;input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
N,K=map(int,input().split());A=array('i',map(int,input().split()));L=min(A);R=max(A);U=sum(A[:K])
while R-L>5e-4:
 M=(R+L)/2;S=U-K*M;T=X=0;Z=S>0
 for i in range(K,N):
  if Z:break
  S+=A[i]-M;T+=A[i-K]-M;X=min(T,X);Z|=S>X
 if Z:L=M
 else:R=M
print(M)