class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        #d.sort(key=lambda x:(-len(x),x))
        maxlength=0
        res=""
        for w in d:
            if self.isSub(w,s):
                res = min((-len(res), res), (-len(w), w))[1]
        return res
    
    def isSub(self,s1,s2):
        j=0
        i=0
        while(i<len(s1) and j<len(s2)):
            if s1[i]==s2[j]:
                i+=1
            j+=1
        return i==len(s1)
    