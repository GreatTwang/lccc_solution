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