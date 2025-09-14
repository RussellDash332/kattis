s=chr(sum(ord(i)-65for i in input())%26+65);d=input();n=int(input());m=2-n%2
if d=='+':a=~-n//2*(~-n//2*' '+s*m+'\n');print(a+(s*n+'\n')*m+a)
elif d=='-':a=~-n//2*'\n';print(a+(s*n+'\n')*m+a)
elif d=='x':
 for i in range(n):v=int(~-n/2-abs(i-~-n/2));print(' '*v+s*m+(' '*abs(n-2*v-2)+s*m)*(2*i+1!=n>2))
else:
 for i in range(n):print(' '*(~i+n)+s*m)