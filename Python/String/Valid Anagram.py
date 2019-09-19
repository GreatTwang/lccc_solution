class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        table={}
        for c in s:
            table[c]=table[c]+1 if c in table else 1
        for c in t:
            if c in table:
                table[c]-=1
            if c not in table or table[c]<0:
                return False
        return True