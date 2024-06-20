import sys; input = sys.stdin.readline; from array import *
class FenwickTree:
    def __init__(self, arr):
        self.ft = [0]*(len(arr)+1); self.n = len(arr)
        for i, e in enumerate(arr): self.add(i+1, e)
    def add(self, idx, e):
        while idx <= self.n: self.ft[idx] += e; idx += idx&(-idx)
    def get(self, idx):
        s = 0
        while idx > 0: s += self.ft[idx]; idx -= idx&(-idx)
        return s
N, Q = map(int, input().split()); F = FenwickTree(A:=array('i', map(int, input().split()))); S = sum(A)
def f(n): return abs(abs(2*F.get(n)+A[n]-S)-(A[n]%2))
for _ in range(Q):
    i, x = map(int, input().split()); a, b = 0, N-1; F.add(i+1, x-A[i]); S += x-A[i]; A[i] = x
    while b-a>2:
        if f(μ:=b-(b-a)//3) > f(λ:=a+(b-a)//3): b = μ
        else: a = λ
    print(min(range(max(0, a-2), min(N, b+3)), key=f))