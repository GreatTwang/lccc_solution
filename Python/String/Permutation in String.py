class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        d1, d2 = dict(), dict()
        for i in range(len(s1)):
            d1[s1[i]] = d1.get(s1[i],0)+1
            d2[s2[i]] = d2.get(s2[i],0)+1
        
        if d1 == d2:
            return True
        
        for i in range(len(s1), len(s2)):
            d2[s2[i]] = d2.get(s2[i],0)+1
            d2[s2[i - len(s1)]] -= 1
            if d2[s2[i - len(s1)]] == 0:
                d2.pop(s2[i - len(s1)])
            if d1 == d2:
                return True
        return False



