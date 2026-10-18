from random import*;S={}
for w in[*open(0)][1:]:print(S.setdefault(eval(w[:w.find('L')]),''.join(sample('abcdefghijkl',9))))