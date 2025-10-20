n,k,*v=map(int,open(0).read().split());a=[i%k+1for i in range(max(v))]
if max(v)-min(v)>k:print('IMPOSSIBLE');exit()
for x in v:print(*a[:x])