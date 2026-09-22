I=lambda:map(int,input().split());n,k=I();D=[0]*-~n
for _ in'.'*k:a,b=I();D[a]+=1;D[b]+=1
print(n*~-n*(n-2)//6-sum(v*(~v+n)for v in D)//2)