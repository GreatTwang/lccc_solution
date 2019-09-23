class MaxStack(object):
    def __init__(self):
        self.num = {}
        self.maxheap = []
        self.idx = -1

    def push(self, x):
        self.idx += 1
        heapq.heappush(self.maxheap, (-x, -self.idx))
        self.num[self.idx] = x

    def pop(self):
        while self.idx not in self.num:
            self.idx -= 1
        res = self.num[self.idx]
        del self.num[self.idx]
        self.idx -= 1
        return res

    def top(self):
        while self.idx not in self.num:
            self.idx -= 1
        return self.num[self.idx]

    def peekMax(self):
        top, idx = - self.maxheap[0][0], - self.maxheap[0][1]
        while idx not in self.num or self.num[idx] != top:
            heapq.heappop(self.maxheap)
            top, idx = - self.maxheap[0][0], - self.maxheap[0][1]
        return top

    def popMax(self):
        top, idx = heapq.heappop(self.maxheap)
        while -idx not in self.num or self.num[-idx] != -top:
            top, idx = heapq.heappop(self.maxheap)
        del self.num[-idx]    
        return -top
        
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()