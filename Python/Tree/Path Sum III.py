class Solution(object):      
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.total = 0
        hmap = {0:1} # stores number of nodes that end with the sum of key (looked up by children of the node)
        self.helper(root, hmap, 0, sum)
        return self.total
        
    def helper(self, root, hmap, runsum, sum):
        
        if not root:
            return 
        runsum += root.val
        if runsum - sum in hmap:
            self.total += hmap[runsum-sum]
        hmap[runsum] = hmap.get(runsum, 0) + 1
        self.helper(root.left, hmap, runsum, sum) 
        self.helper(root.right, hmap, runsum, sum)
        hmap[runsum] -= 1
        
        
#         if not root:
#             return 0
        
#         return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum) 
        
    
#     def helper(self, root, sum):
#         if not root:
#             return 0
        
#         return (root.val == sum) + self.helper(root.left, sum - root.val) + self.helper(root.right, sum - root.val)