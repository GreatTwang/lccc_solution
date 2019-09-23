#  O(log mn)   O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                mid = (left + right) // 2
                midvalue = matrix[mid // n][mid % n]
                if target == midvalue:
                    return True
                else:
                    if target < midvalue:
                        right = mid - 1
                    else:
                        left = mid + 1
        return False