def d(s):
 s = s.replace('^', ':{')
 for i in range(17,0,-1): s = s.replace(str(i),'}'*i)
 return eval(s.replace('#','{.:0').replace('{',"{'").replace(':',"':").replace(',',",'").replace("'",'"').replace('@',"'").replace('!',"'s"))
def f(t,s=[],w=''):
 for k,v in t.items():
  if k=='.':s.append(w)
  else:f(v,s,w+k)
def m(p):s=[];f(d(open(p).read()),s);[*map(print,sorted(s))]
try:m('/src/cc')
except:m('./src/cc')