class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        table={}
        for c in s:
            table[c]=table[c]+1 if c in table else 1
        count=0
        for k,v in table.items():
            if v%2:
                count+=1
            if count>1:
                return False
        return True