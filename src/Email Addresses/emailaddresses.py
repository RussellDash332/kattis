P=print;s=input();K=lambda x:P(x+'.')<exit();A='@'
if A not in s:K('@ symbol is missing')
if s.count(A)>1:k=s.find(A);m=s[k+1:].find(A);P(s);K(' '*(k+1+m)+'^--there is an extra @ symbol here')
if s[0]==A:K('There is nothing before the @ symbol')
if s[-1]==A:P(s);K(' '*len(s)+'^--there is nothing after the @ symbol')
if'.'==s[0]:K('Email address starts with a dot')
if'.'==s[k:=s.find(A)-1]:P(s);K(' '*k+'^--there is an extra dot here')
if~(k:=s.find('..')):P(s);K(' '*k+'^--there are consecutive dots here')
K(['Top-level-domain is missing','All good'][bool(len(k:=s.split(A)[1].split('.'))>1and k[-1])])