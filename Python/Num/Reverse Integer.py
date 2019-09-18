#   O(lg N)   O(1)
class Solution:
    def reverse(self, x: int) -> int:
        maxnum = 2**31-1
        minnum = -2**31
        flag=1
        newx=0
        # if x>=maxnum or x<=minnum:
        #     return 0
        if x<0:
            flag=-1
            x=-x
        while(x!=0):
            rx=x%10
            x=x//10
            newx=newx*10+rx
        if newx>maxnum or newx<minnum:
            return 0
        return newx*flag
        