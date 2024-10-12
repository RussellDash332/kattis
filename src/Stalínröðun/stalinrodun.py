from bisect import*;L=[]
for i in map(int,[*open(0)][1].split()):
 if(b:=bisect(L,-i-1))==len(L):L+=[-i]
 else:L[b]=-i
print(len(L))