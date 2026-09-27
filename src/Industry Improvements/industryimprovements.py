N,K,*A=map(int,open(0).read().split());L=max(A);H=sum(A)
while L<H:
 M=(L+H)//2;s=c=0
 for i in A:
  if i+s>M:c+=1;s=0
  s+=i
 if(s>0)+c<=K:H=M
 else:L=M+1
print(L)