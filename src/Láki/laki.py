class log:
 def __init__(s,v):s.k=eval(str(v))
 def __add__(s,o):return log(s.k*o.k)
 def __repr__(s):return f'log({s.k})'
s=input();o=0;e=exit
for a,b in[['tragedy + time','comedy'],['repetition + repetition','learning'],['fire + water','steam'],['red + blue','purple'],['icelander + deadline','procrastination'],['throat + potato','danish'],['kattis + program','verdict'],['problem + solution','AC'],['contest + geometry','WA'],['nonsense + annoyance','this problem']]:s==a and print(b)<e()
try:r=eval(s)
except:r=None
for t in(int,hex,oct,bin,list,tuple,bool,log,set,dict,str):
 try:
  if all(x==str(t(eval(x)))for x in s.split(' + ')):print(t(r));o=1;break
 except:
  try:
   if all(x==str(t(eval(x)))for x in s.split(' + ')):print(t(sorted(eval(s.replace('+','|')))));o=1;break
  except:pass
if o:e()
if r!=None:print(r);e()
try:
 if not o:r=eval(s.replace('i','j'));print(int(r.real),'+',str(int(r.imag))+'i');o=1
except:pass
if o:e()
a=['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
try:print(a[sum(a.index(i)for i in s.split(' + '))]);o=1
except:pass
if o:e()
m=[0]
for i in s:
 if ord(i)>119519:m[-1]=m[-1]*20+ord(i)-119520
 else:m.append(0)
y=sum(m);z=''
while y:z+=chr(119520+y%20);y//=20
if'mod'not in s:print(z[::-1]or chr(119520));e()
from math import*
def bz(a, b):
 if a==0:return 0,1
 if b==0:return 1,0
 p,q=bz(b,a%b);return q,p-a//b*q
def cr(a,m,b,n):d=gcd(m,n);k=m*n//d;return(a-m*bz(m,n)[0]*(a-b)//d)%k,k
t=s.split()
print(*cr(int(t[0]),int(t[2]),int(t[4]),int(t[6])),sep=' mod ')