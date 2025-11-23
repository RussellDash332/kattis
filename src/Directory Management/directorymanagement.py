import sys;from array import*;from bisect import *;P=sys.stdout.write;M=lambda:P('EMPTY\n');E=lambda:P('ERR\n');G=lambda:P('OK\n');I=sys.stdin.readline
class SortedList:
 def __init__(s,A=None,l1=200,l2=64,mv=~(1<<30)):s.l1=l1;s.l2=l2;s.x1=s.l1*2;s.x2=s.l2*2;s.g1=len(bin(s.x1))-3;s.g2=len(bin(s.x2))-3;s.mv=mv;s.clear()
 def clear(s):s.b=[[]];s.bc=[0];s.bm=[0];s.sm=[];s.ss=[];s.cnt=0
 def __len__(s):return s.cnt
 def _ex(s):
  bo=[*s.b];c=sum(map(bool,bo));sn=(c+s.l2-1)//s.l2;ec=s.cnt;s.clear();s.cnt=ec;s.sm.extend([s.mv]*sn);s.ss.extend([0]*sn);i=0
  for bk in bo:
   if bk:
    s.sm[i>>s.g2-1]=bk[-1];s.ss[i>>s.g2-1]+=1;s.bm.append(bk[-1]);s.bc.append(len(bk));s.b.append(bk);i+=1
    if i&(s.l2-1)==0 and i<c:s.b.extend([]for _ in range(s.l2));s.bc.extend([0]*s.l2);s.bm.extend([0]*s.l2)
  for i in range(1,len(s.bc)):
   if i+(i&-i)<len(s.bc):s.bc[i+(i&-i)]+=s.bc[i]
 def __getitem__(s,k):
  k%=s.cnt;bi=0;i=1<<(len(bin(len(s.bc)-1))-3)
  while i:
   if bi|i<len(s.bc)and k>=s.bc[bi|i]:k-=s.bc[bi:=bi|i]
   i>>=1
  return s.b[bi+1][k]
 def _lb(s,x):
  if not s.ss:return(0,len(s.b[0]))
  l=-1;r=len(s.ss)-1
  while r-l>1:
   if s.sm[m:=(l+r)>>1]>=x:r=m
   else:l=m
  l=r<<s.g2;r=r<<s.g2|s.ss[r]
  while r-l>1:
   if s.bm[m:=(l+r)>>1]>=x:r=m
   else:l=m
  return(r,bisect_left(s.b[r],x))
 def _ub(s,x):
  if not s.ss:return(0,len(s.b[0]))
  l=-1;r=len(s.ss)-1
  while r-l>1:
   if s.sm[m:=(l+r)>>1]>=x:r=m
   else:l=m
  l=r<<s.g2;r=r<<s.g2|s.ss[r]
  while r-l>1:
   if s.bm[m:=(l+r)>>1]>=x:r=m
   else:l=m
  return(r,bisect(s.b[r],x))
 def _rbm(s,b1,b2):
  for i in range(b1,b2+1):s.bc[i]=0
  for i in range(b1,b2+1):
   if s.b[i]:s.bc[i]+=len(s.b[i]);s.bm[i]=s.b[i][-1]
   if i+(i&-i)<=b2:s.bc[i+(i&-i)]+=s.bc[i]
  lo=(-b2&b2)//2
  while lo>=s.x2:s.bc[b2]+=s.bc[b2-lo];lo>>=1
 def index(s,x):
  if not s.ss:return 0
  bi,rk=s._lb(x);i=bi-1
  while i:rk+=s.bc[i];i ^=i&-i
  return rk
 def append(s,x):
  s.cnt+=1
  if not s.ss:s.b.append([x]);s.bc.append(1);s.bm.append(x);s.sm.append(x);s.ss.append(1);return
  bi,it=s._lb(x);i=bi
  while i<len(s.bc):s.bc[i]+=1;i+=i&-i
  s.b[bi].insert(it,x);si=(bi-1)>>s.g2;s.bm[bi]=max(s.bm[bi],x);s.sm[si]=max(s.sm[si],x)
  if len(s.b[bi])>=s.x1:
   bj=(si<<s.g2)|s.ss[si];bn=si+1<<s.g2
   if len(s.b)<=bn:s.b.insert(bi+1,s.b[bi][s.l1:]);s.bc.append(0);s.bm.append(0)
   else:s.b[bi+2:bj+2]=s.b[bi+1:bj+1];s.b[bi+1]=s.b[bi][s.l1:]
   s.b[bi]=s.b[bi][:s.l1];s.ss[si]+=1
   if s.ss[si]==s.x2:s._ex()
   else:s._rbm(si<<s.g2|1,min(bn,len(s.bc)-1))
 def remove(s,x):
  if not s.sm or s.sm[-1]<x:return
  bi,it=s._lb(x)
  if it==len(s.b[bi])or s.b[bi][it]>x:return
  s.cnt-=1;i=bi
  while i<len(s.bc):s.bc[i]-=1;i+=i&-i
  s.b[bi].pop(it);si=(bi-1)>>s.g2;bj=(si<<s.g2)|s.ss[si]
  if s.b[bi]:
   s.bm[bi]=s.b[bi][-1]
   if bi==bj:s.sm[si]=s.b[bi][-1]
  else:
   if len(s.b)<=(bn:=si+1<<s.g2):
    s.b.pop(bi);s.bm.pop(bi);s.bc.pop();s.ss[si]-=1
    if s.ss[si]==0:s.sm.pop();s.ss.pop()
    else:
     s._rbm(si<<s.g2|1,len(s.bc)-1)
     if bi==bj:s.sm[si]=s.b[bj-1][-1]
   else:
    s.ss[si]-=1
    if s.ss[si]==0:s._ex()
    else:
     s.b[bi:bj]=s.b[bi+1:bj+1];s.b[bj]=[];s._rbm(si<<s.g2|1,bn)
     if bi==bj:s.sm[si]=s.b[bj-1][-1]
 def pop(s,k=-1):s.remove(v:=s[k]);return v
def K(x):
 s='';p=3
 while x:s+=chr(x//27**p+96);x%=27**p;p-=1
 return s
def L(s):
 x=0
 for i in range(len(s)):x+=(ord(s[i])-96)*27**(3-i)
 return x
R=L('root');SN=array('i');SP=array('i');SC=[];SS=array('i');SM=[];SZ=array('i');ST=[]
def D(n):
 SN.append(L(n));SP.append(-1);SC.append(SortedList());SS.append(1);SM.append({});SZ.append(0);ST.append([L(n)]);return len(SN)-1
def rb(x):
 ST[x]=[]
 for i in range(len(SC[x])):
  for j in ST[SM[x][SC[x][~i]]]:
   ST[x]+=[j]
   if len(ST[x])==5:return
 if len(ST[x])<5:ST[x]+=[SN[x]]
def mk(x,c):
 SP[c]=x;SM[x][SN[c]]=c;SC[x].append(SN[c]);SS[x]+=SS[c];SZ[x]+=SS[c]
def rm(x,c):
 SP[c]=-1;del SM[x][SN[c]];SC[x].remove(SN[c]);SS[x]-=SS[c];SZ[x]-=SS[c]
def ls(x):
 if not SC[x]:M()
 elif len(SM[x])<11:
  for i in range(len(SC[x])):P(K(SC[x][i])+'\n')
 else:
  for i in range(5):P(K(SC[x][i])+'\n')
  P('...\n')
  for i in range(5):P(K(SC[x][i-5])+'\n')
def df(u,k):
 P(K(SN[u])+'\n');k-=1
 for i in range(len(SC[u])):
  if k<1:return k
  k=df(SM[u][SC[u][i]],k)
 return k
def tr(x):
 if SS[x]<2:M()
 elif SS[x]<11:df(x,SS[x])
 else:
  df(x,5);P('...\n')
  for i in range(len(ST[x])):P(K(ST[x][~i])+'\n')
def f(c,x,v,u=0):
 y=None
 if c<'B':mk(x,v);G()
 elif c<'D':
  s=v[0]
  if s=='..':
   if SN[x]==R:E()
   else:y=('C',[K(SN[x])]);SZ[SP[x]]+=SZ[x];SS[SP[x]]+=SZ[x];SZ[x]=0;x=SP[x];G()
  elif(s:=L(s))in SM[x]:y=('C',['..']);x=SM[x][s];G()
  else:E()
 elif c<'M':ls(x)
 elif c<'N':
  s=v[0]
  if L(s)in SM[x]:E()
  else:mk(x,D(s));y=('R',[s]);G()
 elif c<'S':
  s=v[0]
  if(s:=L(s))in SM[x]:y=('A',d:=SM[x][s]);rm(x,d);G()
  else:E()
 elif c<'T':P(str(SS[x])+'\n')
 else:tr(x)
 return x,(None if u else y)
for _ in'.'*int(I()):
 x=D('root');U=[]
 for _ in'.'*int(I()):
  c,*v=I().strip().split();rb(x)
  if c<'U':x,y=f(c,x,v);U+=[y]if y else[]
  elif U:c,y=U.pop();x,y=f(c,x,y,1)
  else:E()