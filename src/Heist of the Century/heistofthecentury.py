G=[N:=int(input())]*N;f=lambda:print(*G)or int(input())or exit();R=range(N)
for i in R:G[i]=1;v=f();G[i]=2*N;w=f();G[i]=[N,v+1,2*N-w][(v>N)-(w>N)]
for i in R:
 if G[i]==N:G[i]=1;G[i]+=f()
f()