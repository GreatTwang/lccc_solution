class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = []
        def helper(root):
            if not root:
                return
            arr.append(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        arr.sort()
        minDiff = (arr[-1]-arr[0])
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < minDiff:
                minDiff = arr[i] - arr[i-1] 
    
        return minDiff