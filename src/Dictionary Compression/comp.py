import sys, gzip, bz2, zlib
words = list(map(lambda x: x.strip(), open('dict.txt').readlines()))

def add(trie, word):
    ptr = trie
    for i in word.replace("'s", '!').replace("'", "@"):
        if i not in ptr: ptr[i] = {}
        ptr = ptr[i]
    ptr['.'] = 0

trie = {}
[add(trie, word) for word in words[:int(input())]]

def clean(trie):
    s = str(trie).replace("'", '').replace(' ', '').replace('{.:0', '#')
    for i in range(17, 0, -1): s = s.replace('}'*i, str(i))
    return s.replace(':{', '^')

c = clean(trie)
print(f'Trie simplified from {len(str(trie))} to {len(c)} bytes!')

print('Size before compression:', sys.getsizeof(c))
#cc = gzip.compress(bz2.compress(c.encode()))
#print('Size after compression: ', sys.getsizeof(cc))
#print('Compression ratio:      ', sys.getsizeof(c)/sys.getsizeof(cc))
#open('src/cc', 'wb').write(cc)
open('src/cc', 'w').write(c)