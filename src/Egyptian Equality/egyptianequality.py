I=input;N=int(I());M=[[*I()]for _ in'.'*N];S=sum(r.count('C')for r in M)
for x,y in zip(([(N-1,c)for c in range(2*N-1)],[(r,c)for r in range(N)for c in range(max(N-r-1,N+r-2),N+r)],[(r,c)for r in range(N)for c in range(N-r-1,min(N-r+1,N+r))]),(sorted([(r,c)for r in range(N-1)for c in range(N-r-1,N+r)],key=lambda t:(-t[0],-abs(t[1]-N+1))),sorted([(r,c)for r in range(N)for c in range(N-r-1,max(N-r-1,N+r-2))],key=lambda t:(t[0]-t[1],t[0])),sorted([(r,c)for r in range(N)for c in range(min(N-r+1,N+r),N+r)],key=lambda t:(sum(t),t[0]))
)):
  s=0
  if 2*sum(M[r][c]>'B'for r,c in x)<=S:
   for r,c in x:s+=M[r][c]>'B';M[r][c]='B'
   for r,c in y:
    if 2*s==S:break
    s+=M[r][c]>'B';M[r][c]='B'
   for r in range(N):
    for c in range(N-r-1,N+r):
     if M[r][c]!='B':M[r][c]='A'
   for m in M:print(''.join(m))
   exit()
print('impossible')