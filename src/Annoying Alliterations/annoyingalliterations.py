M=max(W:=[*map(str.strip,open(Z:=0))][1:],key=len)
for w in W:
 p=0
 while p<len(w)and w[p]==M[p]:p+=1
 Z=max(Z,len(w)+len(M)-2*p)
print(Z)