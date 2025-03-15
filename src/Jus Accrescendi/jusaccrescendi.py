def f(v):all(v[i]<=len(z[i])for i in range(4))and[print(*z[i][j])for i in range(4)for j in range(v[i])]<exit()
T,B=map(int,input().split());z=[[],[],[],[]];m=1999
for t in range(m):x=t%m;y=t*t%m;z[2*(x%2)+y%2]+=[(x-m//2,y-m//2)]
for a in range(T):
 for b in range(T-a):
  for c in range(T-a-b):T*(T-1)*(T-2)//6==B+a*b*c+a*b*(d:=T-a-b-c)+a*c*d+b*c*d!=f((a,b,c,d))
print('IMPOSSIBLE')<exit()