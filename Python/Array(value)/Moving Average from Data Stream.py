#   O(1)    O(size)
class MovingAverage:
    def __init__(self, size: int):
        self.size=size
        self.currsize=0
        self.window=[]
        self.sum=0
    def next(self, val: int) -> float:
        if self.currsize<self.size:
            self.window.append(val)
            self.currsize+=1
            self.sum+=val
            average= self.sum/self.currsize         
        else:
            self.sum-=self.window[0]
            self.sum+=val
            self.window.pop(0)
            self.window.append(val)
            average= self.sum/self.size
        return average