K=1440;n,*a=map(int,open(0).read().split());f=[0]*K;b=n
for i in a:f[i]+=1
for d in range(1,K):b=min(b,sum(f[i]+sum(max(0,f[j]-f[j-d])for j in range(i+d,K,d))for i in range(d)))
print(b,n)