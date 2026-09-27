I=lambda:map(int,input().split());Z=S=0;N,H=I();Q,R=zip(*[I()for _ in'.'*N],(0,H))
for i in range(N):S+=Q[i];Z+=(R[i+1]-R[i])/S**(1/6)
print(Z/10**1.5)