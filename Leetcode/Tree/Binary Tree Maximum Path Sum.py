class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.dfs(root)
        return self.res
    
    def dfs(self,root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l+r+root.val > self.res:
            self.res = l+r+root.val
        return max(0,root.val+max(l,r))

#####
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        self.max_gain(root)
        return self.max_sum
    def max_gain(self,node):
        if not node:
            return 0

            # max sum on the left and right sub-trees of node
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)
            
            # the price to start a new path where `node` is a highest node
        price_newpath = node.val + left_gain + right_gain
            
            # update max_sum if it's better to start a new path
        self.max_sum = max(self.max_sum, price_newpath)
        
            # for recursion :
            # return the max gain if continue the same path
        return node.val + max(left_gain, right_gain)

