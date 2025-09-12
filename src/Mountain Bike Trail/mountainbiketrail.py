n=int(input());z=[0]*2**20
for _ in'.'*n:
 s=input();i=int(s.split()[0])if'e'<s[-1]else 0
 if z[i+1]:z[i+1]-=1
 z[i]+=1
print(sum(z),n)