# python comp.py | bzip2 > dictionary && python dictionary.py
import bz2, os; w=b''
#print(os.path.getsize('dictionary'))
for x in bz2.open(__file__[:-3]).read().split(b'%'):print((w:=(x and w[:len(w)-x[0]]+x[1:])or w+b"'s").decode())