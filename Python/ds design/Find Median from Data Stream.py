from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = []
        self.larger = []
        self.median = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if num > self.median:
            heappush(self.larger, num)
            if len(self.larger) > (len(self.smaller) + 1):
                a = heappop(self.larger)
                heappush(self.smaller, -a)
            self.median = self.larger[0]
        else:
            heappush(self.smaller, -num)
            if len(self.smaller) > (len(self.larger) + 1):
                a = heappop(self.smaller)
                heappush(self.larger, -a)
            self.median = -self.smaller[0]
                
        if len(self.larger) == len(self.smaller):
            self.median = float(self.larger[0] - self.smaller[0]) / 2
        
    def findMedian(self):
        """
        :rtype: float
        """
        return self.median   