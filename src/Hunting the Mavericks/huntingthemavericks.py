I=lambda:map(int,input().split());N,M=I();D=[0]*-~N;Z=S=0
for _ in'.'*M:a,b=I();D[a]-=1;D[b]+=1;S+=a<b
for i in D:Z=max(Z,S:=S+i)
print(M-Z)