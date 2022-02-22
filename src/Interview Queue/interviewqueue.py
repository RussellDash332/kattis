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
            self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1
    
    def remove(self, node):
        if node.prev:   node.prev.next = node.next
        if node.next:   node.next.prev = node.prev
        if self.tail == node:   self.tail = node.prev
        node.next, node.prev = None, None
        self.size -= 1

    # debug
    def print(self):
        arr = []
        curr = self.tail
        while curr:
            arr.append(curr.val)
            curr = curr.prev
        print(arr[::-1])

n = int(input())
arr = list(map(int, input().split()))
look = list(range(n))
ll, m, count, history = LL(), {}, 0, []

for i in range(n):
    node = Node(i)
    ll.insert(node)
    m[i] = node

while True:
    nxt, rem = set(), set()

    for idx in look:
        # m[idx].val = idx
        if (m[idx].prev and arr[idx] < arr[m[idx].prev.val]) or (m[idx].next and arr[idx] < arr[m[idx].next.val]):
            rem.add(idx)
            if m[idx].prev: nxt.add(m[idx].prev.val)
            if m[idx].next: nxt.add(m[idx].next.val)

    if not rem:
        # no need to sort as it will be only one single value repeated
        k = list(set(look))
        history.append([arr[k[0]]] * ll.size)
        break
    
    look = nxt - rem
    history.append(list(map(lambda x: arr[x], sorted(rem))))
    for i in rem:
        ll.remove(m[i])
    count += 1

print(count)
for r in history:
    print(*r)