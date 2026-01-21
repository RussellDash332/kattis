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
n, m = map(int, input().split()); L = LL(); H = {}
for i in input().split(): L.insert(Node(i)); H[len(H)] = L.tail
for _ in range(m):
    k, x = input().split(); k = int(k); p = H[k]
    if x == 'L': H[k] = p.prev
    elif x == 'R': H[k] = p.next
    else: v = Node(x); L.insert_at(v, p.prev); H[k] = v
c = L.tail.next; z = []
for _ in range(L.size): z.append(c.val); c = c.next
print(' '.join(z))