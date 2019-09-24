class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        j = 0
        maxl=1
        for i in range(1,len(A)):
            if A[i]==A[i-1]:
                j=i
            elif not(i>=2 and (A[i-2]<A[i-1]>A[i] or A[i-2]>A[i-1]<A[i])):
                j=i-1
            maxl=max(maxl,i-j+1)
        return maxl