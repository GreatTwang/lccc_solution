# O(N^2)    O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=0
        r=0
        if len(s)<=1:
            return s
        for i in range(len(s)):
            l1=self.expand(s,i,i)
            l2=self.expand(s,i,i+1)
            length=max(l1,l2)
            if length>r-l:
                l=i-length//2
                r=i+length//2
                print(l,r)
            print(l)
        return s[l:r+1]
        
    def expand(self,s,l,r):
        while (l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        return r-l-1