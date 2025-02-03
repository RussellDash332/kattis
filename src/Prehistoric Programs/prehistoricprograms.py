a=[[],[]];u=[];v=[]
for x in range(int(input())):
 b=z=d=0;s=input()
 for i in s:c=2*(i<')')-1;b+=c;d=max(d,-b)
 a[b<0].append((d+b*(b<0),b,x));v.append(s)
for _,_,x in sorted(a[0])+sorted(a[1])[::-1]:
 u.append(x+1)
 for i in v[x]:
  z+=2*(i<')')-1
  if z<0:print('impossible'),exit()
print('impossible')if z else print(*u)