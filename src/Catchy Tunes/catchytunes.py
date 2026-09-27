N=int(input());F={};O=[*range(0,N,2),*range(1,N,2)];Z=['']*N;p=0
for _ in'.'*N:a,s=input().split();F.setdefault(a,[]).append(s)
for a,t in sorted(F.items(),key=lambda x:-len(x[1])):
 for s in t:Z[O[p]]=s;p+=1
print('\n'.join(Z))