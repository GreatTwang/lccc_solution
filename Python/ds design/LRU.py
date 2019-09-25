# OrderedDict   O(1)    O(capacity)
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

#   dict+double-linked list   O(1)    O(capacity)
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.next = self.head
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            nextNode = self.head.next
            node.next = nextNode
            node.prev = self.head
            nextNode.prev = node
            self.head.next = node    
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
        else:
            if len(self.cache) == self.capacity:
                node = self.tail.prev
                node.prev.next = self.tail
                self.tail.prev = node.prev
                del self.cache[node.key]
            newNode = Node(key, value)
            self.cache[key] = newNode
            nextNode = self.head.next
            nextNode.prev = newNode
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = nextNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)