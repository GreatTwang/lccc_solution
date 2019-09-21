class Solution:
    def intToRoman(self, num: int) -> str:
        A = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        B = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        D = ['','M','MM','MMM']
        
        return D[num//1000]+C[num%1000//100]+B[num%100//10]+A[num%10]

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