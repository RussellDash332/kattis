I=lambda:map(int,input().split());N,M,K=I();G=[0]*N
for _ in'.'*M:x,y=I();x-=1;y-=1;G[x]|=1<<y;G[y]|=1<<x
print('YNEOS'[all(K>(G[x]&G[y]&~(1<<x)&~(1<<y)).bit_count()for x in range(N)for y in range(x))::2])