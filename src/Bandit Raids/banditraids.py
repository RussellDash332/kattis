v=[*map(int,input().split())];p=[]
while min(v):
 t=sorted((v[i],i)for i in(0,1,2));q=t[1][0]//t[0][0]
 while q:v[t[2-q%2][1]]-=v[u:=t[0][1]];v[u]*=2;q//=2;p.append([*v])
print(len(p))
for i in p:print(*i)