class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.next = self.head
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
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
        """
        :type key: int
        :type value: int
        :rtype: void
        """
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