class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        loc = 0
        end = len(s)
        while loc < end-1:
            curr, after = mapping[s[loc]],mapping[s[loc+1]]
            if curr < after:
                total-=curr
                total+=after
                loc+=2
            else:
                total+=curr
                loc+=1
        if loc<end:
            total+=mapping[s[loc]]
        return total

"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""