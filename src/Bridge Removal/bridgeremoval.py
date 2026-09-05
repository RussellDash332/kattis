N=int(input());G=[[]for _ in'.'*N];E=[]
for _ in'.'*~-N:a,b=map(int,input().split());a-=1;b-=1;G[a]+=[b];G[b]+=[a]
Q=[(0,-1)];L=[]
while Q:
 u,p=Q.pop();L+=[u]*(len(G[u])<2)
 for v in G[u]:
  if v-p:Q+=[(v,u)]
for i in range(K:=len(L)//2):E+=[(L[i]+1,L[i+K]+1)]
if len(L)%2:E+=[(L[0]+1,L[-1]+1)]
print(len(E))
for e in E:print(*e)