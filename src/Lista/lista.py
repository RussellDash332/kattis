def lis(arr):
    def upper_bound(sub, idx):
        lo, hi = 0, len(sub) - 1
        while hi > lo:
            mid = (lo + hi) // 2
            if arr[sub[mid]] < arr[idx]: lo = mid + 1
            else: hi = mid
        return hi
    temp = []; par = [None]*len(arr)
    for i in range(len(arr)):
        if not temp or arr[i] > arr[temp[-1]]:
            if temp: par[i] = temp[-1]
            temp.append(i)
        else:
            rep = upper_bound(temp, i); temp[rep] = i
            if rep != 0: par[i] = temp[rep - 1]
    final = []; curr = temp[-1]
    while curr != None: final.append(arr[curr]); curr = par[curr]
    return final[::-1]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class LL:
    def __init__(self):
        self.tail = None
        self.size = 0
    def insert(self, node):
        if self.tail:
            if self.tail.next:
                self.tail.next.prev = node
                node.next = self.tail.next
            self.tail.next = node
            node.prev = self.tail
        else:
            node.prev = node.next = node
        self.tail = node
        self.size += 1
    def insert_at(self, node, at):
        prev, curr, succ = at, node, at.next
        prev.next, curr.prev, curr.next, succ.prev = curr, prev, succ, curr
        if self.tail == prev:
            self.tail = curr
        self.size += 1
    def remove(self, node):
        if node.prev:   node.prev.next = node.next
        if node.next:   node.next.prev = node.prev
        if self.tail == node:   self.tail = node.prev
        node.next, node.prev = None, None
        self.size -= 1
        return node
    def print(self):
        arr = []
        curr = self.tail
        for _ in range(self.size):
            arr.append(curr.val)
            curr = curr.prev
        return arr[::-1]

import sys; input = sys.stdin.readline
from bisect import *
n, m = map(int, input().split())
h = {i:Node(i) for i in range(n)}
ll = LL()
for i in range(n): ll.insert(h[i])
ll.print()
for _ in range(m):
    c, a, b = input().split(); a = int(a)-1; b = int(b)-1
    if c == 'A':
        fr = h[b].prev == ll.tail
        ll.insert_at(ll.remove(h[a]), h[b].prev)
        if fr: ll.tail = h[a].prev
    else: ll.insert_at(ll.remove(h[a]), h[b])
A = ll.print(); L = lis(A); S = [0]*n; eol = L[-1]
print(n-len(L))
for i in L: S[i] = 1
for i in range(n):
    if S[i] == 0:
        p = bisect_right(L, i)
        if p == len(L): print('B', i+1, eol+1); eol = i
        else: print('A', i+1, L[p]+1)