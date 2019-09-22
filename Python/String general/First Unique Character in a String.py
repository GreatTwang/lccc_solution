class Solution:
    def firstUniqChar(self, s: str) -> int:
        table={}
        for c in s:
            table[c]=table.get(c,0)+1
        for i,c in enumerate(s):
            if table.get(c)==1:
                return i
        return -1