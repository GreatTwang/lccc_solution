class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        a = 5
        while n // a > 0:
            ret += n//a
            a *= 5 
        return ret