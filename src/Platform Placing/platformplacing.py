N,L,H,*A=map(int,open(0).read().split());P=[[2*i-L,2*i+L]for i in sorted(A)]
for i in range(N):
 B=H-L
 if i:B=min(B,P[i][0]-P[i-1][1])
 if i<N-1:B=min(B,P[i+1][0]-P[i][1])
 B<0!=print(-1)>exit();P[i][0]-=B;P[i][1]+=B
print(sum(b-a for a,b in P)//2)