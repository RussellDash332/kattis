c,t,r,p=map(eval,open(0).read().split());T=[w:=0]+[w:=(w+1+p*r)/(1-p)for _ in'.'*c];D=[*T]
for x in range(1,c+1):
 for k in range(x):D[x]=min(D[x],D[k]+t+T[x-k])
print(D[c]+t)