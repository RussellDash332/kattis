from ctypes import *
class mpz(Structure): _fields_ = [('alloc', c_int), ('size', c_int), ('d', c_void_p)]
g = CDLL('libgmp.so.10')
init = g.__gmpz_init; init.argtypes = [c_void_p]
set_str = g.__gmpz_set_str; set_str.argtypes = [c_void_p, c_char_p, c_int]
get_str = g.__gmpz_get_str; get_str.argtypes = [c_char_p, c_int, c_void_p]; get_str.restype = c_char_p

import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, X = map(int, input().split()); S = input().strip(); M = 1<<20; K = 1<<25; bm = M-1; mk = K-1
def f(r, n):
    if n == 0: return 0, 1
    if n&1: s, p = f(r, n-1); return (s+p)%K, p*r%K
    s, p = f(r, n>>1); return s*(1+p)%K, p*p%K
t, _ = f(pow(33, X, K), X); c0 = (t+((t-X)%K)//32)%M

p = [1]
while len(p) < X: q = pow(33, len(p), K); p += [x*q&mk for x in p]
del p[X:]

init(byref(A:=mpz())); set_str(byref(A), ''.join(map(str, [(x*c0+X*((x-1)>>5))&bm for x in p])).encode(), 10)
n = min(len(S), len(z:=get_str(None, 27, byref(A))))
sys.stdout.write((int.from_bytes(S[:n].translate(bytes([c-65 if 65<=c<91 else 26 for c in range(256)])), 'big')+int.from_bytes(z[:n].translate(bytes([c-48 if 48<=c<58 else c-87 if 97<=c<114 else 0 for c in range(256)])), 'big')).to_bytes(n, 'big').translate(bytes([32 if v%27==26 else 65+v%27 for v in range(256)])).decode())