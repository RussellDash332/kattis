for k in[*open(0)][1:]:
 k=k.strip();b=c=['N','NE','E','SE','S','SW','W','NW'].index(k[-2:]);t=2
 for i in k[-3::-1]:b+=(2*['NE','ES','SW','WN'][c//2].index(i)-1)/t;t*=2
 print(b*45)