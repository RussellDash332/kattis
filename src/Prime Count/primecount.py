n=int(input())
v,r,j=int(n**0.5),n-1,1
h,l,u=[0]*(v+1),[0]*(v+1),[0]*(v+1)
for p in range(2,v+1):l[p],h[p]=p-1,n//p-1
for p in range(2,v+1):
    if l[p]==l[p-1]:continue
    t,e=l[p-1],min(v,n//(p*p))
    r-=h[p]-t
    for i in range(p+j,e+1,j):
        if u[i]:continue
        d,x=i*p,((i*p)>v)&1
        h[i]-=[h,l][x][[d,n//d][x]]-t
    for i in range(v,p*p-1,-1):l[i]-=l[i//p]-t
    for i in range(p*p,e+1,p):u[i]=1
    if p==2:j+=1
print(r)