class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter=[]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.counter.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.counter:
            if self.counter[0]<=timestamp-300:
                self.counter.pop(0)
            else:
                break
        return len(self.counter)

#sol2
class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter=dict()        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if timestamp not in self.counter:
            self.counter[timestamp]=1
        else:
            self.counter[timestamp]+=1
        
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        count=0
        for k in self.counter.keys():
            if k>=timestamp-300+1:
                count+=self.counter[k]
                
        return count