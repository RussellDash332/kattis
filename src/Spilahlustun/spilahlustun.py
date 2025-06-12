from random import *

def update(t):
    if t != -1: C[t] = (C[L[t]] if L[t] != -1 else 0) + (C[R[t]] if R[t] != -1 else 0) + 1
def push(t):
    if t != -1 and Z[t]:
        Z[t] = 0; L[t], R[t] = R[t], L[t]
        if L[t] != -1: Z[L[t]] ^= 1; V[L[t]] *= -1
        if R[t] != -1: Z[R[t]] ^= 1; V[R[t]] *= -1
def split(t, val, add=0):
    if t == -1: return -1, -1
    else:
        push(t)
        if val <= (k:=add+(C[L[t]] if L[t] != -1 else 0)):
            l, L[t] = split(L[t], val, add); update(t); return l, t
        else:
            R[t], r = split(R[t], val, k+1); update(t); return t, r
def merge(l, r):
    push(l), push(r)
    if (l == -1) or (r == -1): t = l if l != -1 else r
    elif P[l] < P[r]: R[l] = merge(R[l], r); t = l
    else: L[r] = merge(l, L[r]); t = r
    update(t); return t
def insert(t, val):
    l, r = split(t, 10**9); return merge(merge(l, val), r)
def reverse(t, a, b):
    t1, t2 = split(t, a); t2, t3 = split(t2, b-a)
    if t2 != -1: Z[t2] ^= 1; V[t2] *= -1
    return merge(merge(t1, t2), t3)
def inorder(t):
    if t != -1: push(t), inorder(L[t]), sys.stdout.write(str(V[t])+' '), inorder(R[t])

import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
n, q = map(int, input().split()); treap = -1; V = array('i', range(1, n+1)); L = array('i', [-1]*n); R = array('i', [-1]*n); P = array('i', (randint(1, 10**9) for _ in range(n))); Z = array('b', [0]*n); C = array('i', [0]*n)
for i in range(n): treap = insert(treap, i)
for _ in range(q): i, j = map(int, input().split()); treap = reverse(treap, i-1, j)
inorder(treap)