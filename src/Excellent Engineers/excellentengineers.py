import sys; input = sys.stdin.readline; from array import *; INF = 10**9

class Vertex:
    def __init__(self, v):
        self.key, self.left, self.right, self.parent = v, None, None, None
        self.height, self.size = 0, 1

class AVL:
    def __init__(self):
        self.root = None
    def search(self, v):
        res = self.helper_search(self.root, v)
        return res.key if res != None else INF
    def helper_search(self, t, v):
        if t == None: return None
        elif t.key == v: return t
        elif t.key < v: return self.helper_search(t.right, v)
        return self.helper_search(t.left, v)
    def find_min(self):
        return self.helper_find_min(self.root)
    def helper_find_min(self, t):
        if t == None: return INF
        if t.left == None: return t.key
        return self.helper_find_min(t.left)
    def successor(self, v):
        return self.helper_successor_plus(self.helper_search(self.root, v))
    def helper_successor_plus(self, t):
        if t.right != None: return self.helper_find_min(t.right)
        else:
            par, cur = t.parent, t
            while par != None and cur == par.right: cur, par = par, par.parent
            if par == None: return INF
            else: return par.key
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
    def delete(self, v):
        def helper(t, v):
            if t == None: return t
            if t.key < v: t.right = helper(t.right, v)
            elif t.key > v: t.left = helper(t.left, v)
            else:
                if t.left == None and t.right == None:      t = None
                elif t.left == None and t.right != None:    t.right.parent = t.parent; t = t.right
                elif t.left != None and t.right == None:    t.left.parent = t.parent; t = t.left
                else: successor_v = self.successor(v); t.key = successor_v; t.right = helper(t.right, successor_v)
            if t != None: self.update_height(t), self.update_size(t); t = self.rebalance(t)
            return t
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

for t in range(int(input())):
    n = int(input()); s = []; h = array('i', [-1]*n)
    for _ in range(n): a, b, c = map(int, input().split()); s.append((a-1, c)); h[a-1] = b
    s.sort(key=lambda x: x[1]); p = AVL(); z = 0
    for a, _ in s:
        p.insert(a); k = p.predecessor(a)
        if k != -1 and h[k] < h[a]: p.delete(a); continue
        z += 1
        while True:
            v = p.successor(a)
            if v == INF or h[v] < h[a]: break
            p.delete(v)
    print(z)