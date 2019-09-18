class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.d = 1
        self.depth(root)
        return self.d -1
    
    def depth(self,node):
        if node==None:
            return 0
        l = self.depth(node.left)
        r = self.depth(node.right)
        self.d = max(l+r+1, self.d)
        return max(l,r)+1