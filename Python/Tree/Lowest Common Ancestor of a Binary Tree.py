class Solution(object):
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        if self.isParent(p, q):
            return p
        if self.isParent(q, p):
            return q
        curr=root
        while curr:
            if self.isParent(curr.left, p) and self.isParent(curr.left, q):
                curr = curr.left
            elif self.isParent(curr.right, p) and self.isParent(curr.right, q):
                curr = curr.right
            else:
                return curr
        return root
        
    
    def isParent(self, p, c):
        if not p:
            return False
        if p == c:
            return True
        return self.isParent(p.left, c) or self.isParent(p.right, c)