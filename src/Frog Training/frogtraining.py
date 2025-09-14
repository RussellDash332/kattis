*x,h=map(int,open(0).read().split());d=[1]+[0]*h
for i in x:
 for j in range(h+1-i):d[i+j]+=d[j]
print(d[h])