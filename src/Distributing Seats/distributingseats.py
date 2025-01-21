class Vertex:
    def __init__(self, v):
        self.key, self.left, self.right, self.parent = v, None, None, None
        self.height, self.size, self.count = 0, 1, 1

class AVL:
    def __init__(self):
        self.root = None
    def search(self, v):
        res = self.helper_search(self.root, v)
        return res.key if res != None else -10
    def helper_search(self, t, v):
        if t == None: return None
        elif t.key == v: return t
        elif t.key < v: return self.helper_search(t.right, v)
        return self.helper_search(t.left, v)
    def find_min(self):
        return self.helper_find_min(self.root)
    def helper_find_min(self, t):
        if t == None: return None
        if t.left == None: return t
        return self.helper_find_min(t.left)
    def successor(self, v):
        self.insert(v); k = self.helper_successor_plus(self.helper_search(self.root, v)); self.delete(v); return k
    def helper_successor_plus(self, t):
        if t.right != None: return self.helper_find_min(t.right)
        else:
            par, cur = t.parent, t
            while par != None and cur == par.right: cur, par = par, par.parent
            return par
    def update_height(self, t):
        if t.left != None and t.right != None: t.height = max(t.left.height, t.right.height) + 1
        elif t.left != None: t.height = t.left.height + 1
        elif t.right != None: t.height = t.right.height + 1
        else: t.height = 1
    def update_size(self, t):
        if t.left != None and t.right != None: t.size = t.left.size + t.right.size + t.count
        elif t.left != None: t.size = t.left.size + t.count
        elif t.right != None: t.size = t.right.size + t.count
        else: t.size = t.count
    def balance_factor(self, t):
        if t.left != None and t.right != None: return t.left.height - t.right.height
        elif t.left != None: return t.left.height + 1
        elif t.right != None: return -1 - t.right.height
        return 0
    def insert(self, v, count=1):
        def helper(t, v):
            if t == None: x = Vertex(v); x.count = count; return x
            if t.key < v: t.right = helper(t.right, v); t.right.parent = t
            elif t.key > v: t.left = helper(t.left, v); t.left.parent = t
            else: t.count += count
            self.update_height(t), self.update_size(t); t = self.rebalance(t); return t
        self.root = helper(self.root, v)
    def delete(self, v, count=1):
        def helper(t, v, count):
            if t == None: return t
            if t.key < v: t.right = helper(t.right, v, count)
            elif t.key > v: t.left = helper(t.left, v, count)
            else:
                if t.count <= count:
                    if t.left == None and t.right == None:      t = None
                    elif t.left == None and t.right != None:    t.right.parent = t.parent; t = t.right
                    elif t.left != None and t.right == None:    t.left.parent = t.parent; t = t.left
                    else: successor_v = self.successor(v); t.key = successor_v.key; t.count = successor_v.count; t.right = helper(t.right, successor_v.key, successor_v.count)
                else: t.count -= count
            if t != None: self.update_height(t), self.update_size(t); t = self.rebalance(t)
            return t
        self.root = helper(self.root, v, count)
    def rebalance(self, t):
        if t == None: return t
        if self.balance_factor(t) == 2:
            if self.balance_factor(t.left) == -1: t.left = self.left_rotate(t.left)
            t = self.right_rotate(t)
        elif self.balance_factor(t) == -2:
            if self.balance_factor(t.right) == 1: t.right = self.right_rotate(t.right)
            t = self.left_rotate(t)
        return t
    def left_rotate(self, t):
        w = t.right; w.parent = t.parent; t.parent = w; t.right = w.left
        if w.left != None: w.left.parent = t
        w.left = t; self.update_height(t), self.update_size(t), self.update_height(w), self.update_size(w); return w
    def right_rotate(self, t):
        w = t.left; w.parent = t.parent; t.parent = w; t.left = w.right
        if w.right != None: w.right.parent = t
        w.right = t; self.update_height(t), self.update_size(t), self.update_height(w), self.update_size(w); return w

import sys; input = sys.stdin.readline; from array import *
avl = AVL(); n, r, c = map(int, input().split()); A = array('i', [0]*r); Q = []
for _ in range(n): a, _, s = map(int, input().split()); Q.append((max(min(a-1+s, r-1), 0), max(min(a-1-s, r-1), 0)))
for i in range(r): avl.insert(i, c)
for y, x in sorted(Q):
    if avl.search(z:=x) == x or -1 < (z:=z.key if (z:=avl.successor(x)) else -10) <= y: A[z] += 1; avl.delete(z)
print(sum(A))