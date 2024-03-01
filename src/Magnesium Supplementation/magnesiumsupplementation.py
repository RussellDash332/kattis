n,k,p=map(int,input().split());a=set()
for i in range(1,int(n**0.5)+1):
 if n%i==0:
  if(n+p-1)//p<=i<=k:a.add(i)
  if n//i<=k:a.add(n//i)
print(len(a),*sorted(a))