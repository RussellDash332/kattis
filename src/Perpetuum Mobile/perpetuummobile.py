from math import*;I=lambda:map(eval,input().split());N,M=I();E=[];D=[1]*N
for _ in'.'*M:a,b,c=I();E+=[(a-1,b-1,log(c))]
for _ in'.'*~-N:
 for a,b,w in E:D[b]=min(D[b],D[a]-w)
print('in'*any(D[b]>D[a]-w for a,b,w in E)+'admissible')