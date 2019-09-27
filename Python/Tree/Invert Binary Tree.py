#   O(N)    O(h)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)
        root.left=right
        root.right=left
        return root