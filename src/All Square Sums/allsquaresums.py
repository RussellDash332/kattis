def corn(p):
 q=p-1;s=0
 if p<3:return(1,q)
 while 1-q%2:q//=2;s+=1
 for z in range(2,p):
  if p-1==pow(z,p//2,p):break
 c=pow(z,q,p);r=pow(-1,(q+1)//2,p);t=pow(-1,q,p);m=s
 while(t-1)%p:
  u=t*t%p
  for i in range(1,m):
   if u%p==1:break
   u=u*u%p
  b=pow(c,1<<(m-i-1),p);r=r*b%p;c=b*b%p;t=t*c%p;m=i
 z=[p,min(r,p-r)]
 while z[-1]**2>=p:z.append(z[-2]%z[-1])
 return(z[-1],round((p-z[-1]**2)**0.5))
import subprocess
p=int(input());z=[];k=1
if p==0:print('1\n0^2 + 0^2 = 0'),exit(0)
for f in map(int, subprocess.check_output(f"factor {p}|cut -d':' -f2",shell=True).split()):
 if f%4==3:k*=f
 else:z.append(corn(f))
Z={(0,1)};g=lambda x:f'({x})'if x<0else x
for a,b in z:
 X=set()
 for c,d in Z:t=(abs(a*c-b*d),abs(a*d+b*c));u=(abs(a*c+b*d),abs(a*d-b*c));X.add((min(t),max(t)));X.add((min(u),max(u)))
 Z=X
if(K:=round(k**0.5))**2-k:print(0),exit(0)
W=set()
for a,b in Z:
 for c in(-K,K):
  for d in(-K,K):W.add((a*c,b*d));W.add((b*d,a*c))
print(len(W))
for a,b in W:print(f'{g(a)}^2 + {g(b)}^2 = {p}')