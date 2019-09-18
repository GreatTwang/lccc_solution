class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right :
            return (root.val == sum)

        else:
            return self.hasPathSum(root.left,sum-root.val) \
                or self.hasPathSum(root.right,sum-root.val)