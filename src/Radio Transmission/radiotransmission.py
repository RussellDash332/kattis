N=int(input());S=input();b=[j:=-1]+[i:=0]*N
while i<N:
 while j>=0!=S[i]!=S[j]:j=b[j]
 i+=1;j+=1;b[i]=j
print(i-b[i])