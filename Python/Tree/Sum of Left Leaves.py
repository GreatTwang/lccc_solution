class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        res = 0
        while q:
            node = q.pop(0)
            if node.left:
                if not node.left.left and not node.left.right:
                    res+= node.left.val            
                q.append(node.left) 
            if node.right:
                q.append(node.right) 
 
        return res