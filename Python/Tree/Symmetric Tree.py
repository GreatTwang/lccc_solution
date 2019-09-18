class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.check(root.left,root.right)
        
    def check(self,left,right):
        if (left == None or right == None):
            return left == right
        if left.val != right.val:
            return False
        return self.check(left.left, right.right) and self.check(left.right, right.left)