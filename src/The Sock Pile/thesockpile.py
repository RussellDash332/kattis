m, n = map(int, input().split()); H = [0]*501**3
for s in range(m+n+1):
    for pairs in range(min(s, m)+1):
        for whites in range(min(s-pairs, n)+1):
            if not pairs and whites<2: continue
            singles = s-pairs-whites; k = 251001*pairs+501*whites+singles; p = whites*(whites-1)/2+pairs
            if pairs>1: p += (2*pairs)*(2*pairs-2)/2 * H[k-502000]
            if pairs and whites: p += (2*pairs)*whites * H[k-251501]
            if pairs and singles: p += (2*pairs)*singles * H[k-251001]
            if whites and singles: p += whites*singles * H[k-502]
            if singles>1: p += singles*(singles-1)/2 * H[k-2]
            H[k] = 2*p/(2*pairs+whites+singles)/(2*pairs+whites+singles-1)
print(1-H[251001*m+501*n])