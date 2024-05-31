import sys; input = sys.stdin.readline; from array import *

class Vertex:
    def __init__(self, v):
        self.key, self.left, self.right, self.parent = v, None, None, None
        self.height, self.size = 0, 1

class AVL:
    def __init__(self):
        self.root = None
    def search(self, v):
        res = self.helper_search(self.root, v)
        return res.key if res != None else -1
    def helper_search(self, t, v):
        if t == None: return None
        elif t.key == v: return t
        elif t.key < v: return self.helper_search(t.right, v)
        return self.helper_search(t.left, v)
    def find_max(self):
        return self.helper_find_max(self.root)
    def helper_find_max(self, t):
        if t == None: return -1
        if t.right == None: return t.key
        return self.helper_find_max(t.right)
    def predecessor(self, v):
        return self.helper_predecessor_plus(self.helper_search(self.root, v))
    def helper_predecessor_plus(self, t):
        if t.left != None: return self.helper_find_max(t.left)
        else:
            par, cur = t.parent, t
            while par != None and cur == par.left: cur, par = par, par.parent
            if par == None: return -1
            else: return par.key
    def update_height(self, t):
        if t.left != None and t.right != None: t.height = max(t.left.height, t.right.height) + 1
        elif t.left != None: t.height = t.left.height + 1
        elif t.right != None: t.height = t.right.height + 1
        else: t.height = 1
    def update_size(self, t):
        if t.left != None and t.right != None: t.size = t.left.size + t.right.size + 1
        elif t.left != None: t.size = t.left.size + 1
        elif t.right != None: t.size = t.right.size + 1
        else: t.size = 1
    def balance_factor(self, t):
        if t.left != None and t.right != None: return t.left.height - t.right.height
        if t.left != None: return t.left.height + 1
        if t.right != None: return -1 - t.right.height
        return 0
    def insert(self, v):
        def helper(t, v):
            if t == None: return Vertex(v)
            if t.key < v: t.right = helper(t.right, v); t.right.parent = t
            elif t.key > v: t.left = helper(t.left, v); t.left.parent = t
            self.update_height(t), self.update_size(t); t = self.rebalance(t); return t
        self.root = helper(self.root, v)
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

for _ in range(int(input())):
    n = int(input()); p = AVL(); z = array('b', [0]*n)
    for k in array('i', [int(input()) for _ in range(n)][::-1]): p.insert(k); z[k-1] = p.predecessor(k) != -1
    print(sum(z), *(i+1 for i in range(n) if z[i]))