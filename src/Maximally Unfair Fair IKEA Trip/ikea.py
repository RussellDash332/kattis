k=int(input());n=int(input());s=[]
for _ in range(n):a,b=input().split();s.append((int(b),a))
s.sort(key=lambda x:x[0]);c=(n+k-1)//k;s=s[:(n+(k-1)*(sum(x[0]for x in s[:c])<sum(x[0]for x in s[c:c+n//k])))//k];print(sum(x[0]for x in s),*sorted(x[1]for x in s))