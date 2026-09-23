import re;K=lambda:re.findall('<[^/][^>]*>',input())
for _ in'.'*int(input()):
 A=K();B=K()
 if A==B:print('identical')
 elif all(a.lower()==b.lower()for a,b in zip(A,B)):print('similar',*(a[1:-1].split()[0].lower()*(a!=b)for a,b in zip(A,B)))
 else:print('different')