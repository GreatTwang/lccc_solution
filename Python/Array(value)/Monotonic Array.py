class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        asc = True
        desc = True
        
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                asc = False
            if A[i] > A[i - 1]:
                desc = False
            
        return asc or desc