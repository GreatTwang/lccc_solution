class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        l=1
        r=x
        while(l<=r):
            mid =l+(r-l)//2
            if mid**2>x:
                r=mid-1
            if mid**2<x:
                l=mid+1
            if mid**2==x:
                return mid
        return r
#sol2
from math import e, log
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right