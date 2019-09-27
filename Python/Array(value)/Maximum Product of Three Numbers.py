#   O(N)    O(1)
#   max1*max2*max3
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1=max2=max3=float('-inf')
        min1=min2=float('inf')
        for n in nums:
            if n>max3:
                if n>max2:
                    if n>max1:
                        max3=max2
                        max2=max1
                        max1=n
                    else:
                        max3=max2
                        max2=n
                else:
                    max3=n
            if n<min2:
                if n<min1:
                    min2=min1
                    min1=n
                else:
                    min2=n
        return max(min1*min2*max1,max1*max2*max3)
            