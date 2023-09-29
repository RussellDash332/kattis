import sys, gzip, bz2, zlib, os
words = list(map(lambda x: x.strip(), open('dict.txt').readlines()))
ss = last = ''; delim = '%'
for word in words:
    ss += '%'; i = 0
    while i < min(len(word), len(last)):
        if word[i] != last[i]: break
        i += 1
    if word[i:] != "'s" or last[i:]:
        prefix = chr(len(last)-i)
        ss += prefix + word[i:]
    last = word
c = ss[1:]
print(c, end=''), exit(0)
cc = bz2.compress(c.encode())
path = 'dictionary'
print('Size before compression:', sys.getsizeof(c))
print('Trying', delim, '...', sys.getsizeof(cc))
print('Compression ratio:', sys.getsizeof(c)/sys.getsizeof(cc))
open(path, 'wb').write(cc)
print('Done, file size is', os.path.getsize(path))