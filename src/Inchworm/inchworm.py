k,n,m,*h,b,f=map(int,open(0).read().split());f=h.index(f)
while f<k-1:
 if n<=h[f]-h[b+1]<=m:b+=1
 elif n<=h[f+1]-h[b]<=m:f+=1
 else:break
print(h[f])