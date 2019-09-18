class Solution(object):
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        if self.isParent(p, q):
            return p
        if self.isParent(q, p):
            return q
        while root:
            if self.isParent(root.left, p) and self.isParent(root.left, q):
                root = root.left
            elif self.isParent(root.right, p) and self.isParent(root.right, q):
                root = root.right
            else:
                return root
        return root
        
    
    def isParent(self, p, c):
        if not p:
            return False
        if p == c:
            return True
        return self.isParent(p.left, c) or self.isParent(p.right, c)
        
        ''' # recursive
        if root in (None, p, q):
            return root
        
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        
        if left and right:
            return root
        return left or right
        '''