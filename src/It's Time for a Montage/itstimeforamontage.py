N,*V=map(int,open(d:=0).read().split())
while[i+d for i in V[:N]]<V[N:]:d+=1
print(d)