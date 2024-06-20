N,*T=map(int,open(0).readlines());D=[0]
for i in range(N):D+=[min(D[i-k]+max(T[i]-T[i-k]-1800,20*k)+140for k in range(i+1))]
print(D[N])