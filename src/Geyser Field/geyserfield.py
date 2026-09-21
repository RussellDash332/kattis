N,*A=map(int,open(0));M=1e9
for k in range(1,N):
 a=A[k]-A[0];v=1;c=A[0]
 while c<=A[-1]:
  if c not in A:v=0
  c+=a
 if v and a<=1e5:M=min(M,c)
print(M)