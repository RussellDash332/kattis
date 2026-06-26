s='🧦';T={(0,0)}
for i in open(0).read().split()[1:]:T={(x,y)for x,y in{(x+a*(i<s),y+b*(i>=s))for x,y in T for a in(-1,1)for b in(-1,1)}if-1<x<=y<3}
print('ó'*((2,2)not in T)+'gilt')