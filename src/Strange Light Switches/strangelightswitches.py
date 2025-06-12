n=int(input());s=[*map(int,input())];z=[];S=sum(s)
if 0 not in s:s[0]=0;z.append(0)
p=s.index(0);o=[];e=[]
while s[p]==0:p+=1;p%=n
q=p
while 1:
 r=p
 while s[p]==1:p+=1;p%=n
 k=(p-r)%n;[e,o][k%2].append((r,k))
 while s[p]==0:p+=1;p%=n
 if p==q:break
for r,k in o:
 S-=k
 for i in range(k//2):z.append(v:=(r+2*i+1)%n);s[v]=0
 for i in range(k//2+1):z.append(v:=(r+2*i)%n);s[v]=0
for r,k in e:
 S-=k-2
 for i in range(k//2-1):z.append(v:=(r+2*i+1)%n);s[v]=0
 for i in range(k//2-1):z.append(v:=(r+2*i)%n);s[v]=0
p=s.index(0)
while S:
 while s[p]==0:p+=1;p%=n
 if s[(p-1)%n]+s[(p-2)%n]:print(-1);exit()
 S-=2;z.extend([(p-1)%n,p,(p-1)%n,(p+1)%n]);s[p]=s[z[-1]]=0
print(len(z),*z)