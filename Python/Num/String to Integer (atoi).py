class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.lstrip()
        if not s: 
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in ('-', '+'): s = s[1:]
        res = 0 
        for char in s:
            if char.isdecimal():
                res = res * 10 + ord(char) - ord('0')
            else:
                break
        return max(-2**31 , min(sign*res, 2**31-1))