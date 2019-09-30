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
    def __init__(self,k,v):
        self.key=k
        self.val=v
        self.prev=None
        self.next=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.cache={}
        self.head.next=self.tail
        self.tail.next=self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            nextnode=self.head.next
            self.head.next=node
            node.prev=self.head
            node.next=nextnode
            nextnode.prev=node
            return node.val
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val=value
            self.get(key)
        else:
            if len(self.cache)==self.capacity:
                node=self.tail.prev
                node.prev.next=self.tail
                self.tail.prev=node.prev
                del self.cache[node.key]
            newnode=Node(key,value)
            self.cache[key]=newnode
            nextnode=self.head.next
            self.head.next=newnode
            newnode.prev=self.head
            newnode.next=nextnode
            nextnode.prev=newnode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)